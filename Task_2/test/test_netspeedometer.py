import unittest
from unittest.mock import patch, Mock
from Task_2.netspeedometer.netspeedometer import NetSpeedometer

class TestNetSpeedometer(unittest.TestCase):
    def setUp(self):
        self.host = "localhost"
        self.user = "my_user"
        self.password = "my_password"
        self.option = "-o"
        self.bandwidth_tester = "iperf3"
        self.speedometer = NetSpeedometer(self.host, self.user, self.password, self.option, bandwidth_tester=self.bandwidth_tester)

    @patch('Task_2.netspeedometer.NetSpeedometer.exec_command')
    def test_wait_server_loading_timeout(self, mock_exec_cmd):
        mock_exec_cmd.return_value = ('', '', -1)
        with self.assertRaises(TimeoutError):
            self.speedometer.wait_server_loading()

    @patch("subprocess.Popen")
    @patch("threading.Thread")
    def test_exec_iperf(self, mock_thread, mock_popen):
        mock_process = Mock()
        mock_process.communicate.return_value = (b"iperf3 output", b"iperf3 error")
        mock_process.returncode = 0
        mock_popen.return_value = mock_process

        mock_thread_instance = Mock()
        mock_thread.return_value = mock_thread_instance

        stdout, stderr, returncode = self.speedometer.exec_iperf()

        # Assertions
        self.assertEqual(stdout, b"iperf3 output")
        self.assertEqual(stderr, b"iperf3 error")
        self.assertEqual(returncode, 0)

        mock_thread.assert_called_once_with(target=self.speedometer.exec_command, args=("iperf3 -s -1",))
        mock_thread_instance.start.assert_called_once()


if __name__ == "__main__":
    unittest.main()

