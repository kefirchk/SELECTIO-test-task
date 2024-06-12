import unittest
from unittest.mock import patch, Mock
import subprocess
from Task_2.netspeedometer.sshpass_module.sshpass_interface import SshpassInterface


class TestSSHPASSInterface(unittest.TestCase):
    def setUp(self):
        self.ssh_interface = SshpassInterface(host='testhost.com', user='testuser', password='testpass',
                                              pass_option='-p')

    @patch('subprocess.Popen')
    def test_exec_command(self, mock_popen):
        mock_process = mock_popen.return_value
        mock_process.communicate.return_value = (b'output', b'error')
        mock_process.returncode = 0

        stdout, stderr, returncode = self.ssh_interface.exec_command('ls -l')

        mock_popen.assert_called_once_with('sshpass -p testpass ssh testuser@testhost.com ls -l',
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE, shell=True)
        self.assertEqual(stdout, 'output')
        self.assertEqual(stderr, 'error')
        self.assertEqual(returncode, 0)

    def test_wait_loading(self):
        self.ssh_interface.exec_command = Mock(return_value=("", "", -1))
        self.ssh_interface.wait_loading("iperf3")
        self.ssh_interface.exec_command.assert_called_with("pgrep iperf3")

    def test_stop_process(self):
        self.ssh_interface.exec_command = Mock(return_value=("", "", 0))
        self.ssh_interface.process = Mock(return_value=3333)
        self.ssh_interface.stop_process("iperf3")
        self.ssh_interface.exec_command.assert_called_once_with("pkill iperf3")


if __name__ == '__main__':
    unittest.main()
