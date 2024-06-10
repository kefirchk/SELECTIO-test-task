import unittest
from unittest.mock import patch
import subprocess
from Task_2.netspeedometer.sshpass_module.sshpass_interface import SSHPASSInterface

class TestSSHPASSInterface(unittest.TestCase):
    def setUp(self):
        self.ssh_interface = SSHPASSInterface(host='testhost.com', user='testuser', password='testpass')

    @patch('subprocess.Popen')
    def test_exec_command(self, mock_popen):
        mock_process = mock_popen.return_value
        mock_process.communicate.return_value = (b'output', b'error')
        mock_process.returncode = 0

        stdout, stderr, returncode = self.ssh_interface.exec_command('ls -l')

        mock_popen.assert_called_once_with('sshpass -p testpass ssh testuser@testhost.com ls -l', stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE, shell=True)
        self.assertEqual(stdout, 'output')
        self.assertEqual(stderr, 'error')
        self.assertEqual(returncode, 0)


if __name__ == '__main__':
    unittest.main()
