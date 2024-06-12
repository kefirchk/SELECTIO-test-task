import unittest
from unittest.mock import patch, Mock
from Task_2.netspeedometer.netspeedometer import NetSpeedometer


class TestNetSpeedometer(unittest.TestCase):
    @patch('argparse.ArgumentParser.parse_args')
    def setUp(self, mock_args):
        mock_args.return_value = Mock(server_password='1234',
                                      server_pass_file_name=None,
                                      client_password='5678',
                                      client_pass_file_name=None,
                                      server_user='alex',
                                      client_user='bob',
                                      server_ip='192.168.0.3',
                                      client_ip='192.168.0.4')
        self.speedometer = NetSpeedometer(mock_args)

    @patch("threading.Thread")
    def test_exec_iperf(self, mock_thread):
        mock_thread_instance = Mock()
        mock_thread.return_value = mock_thread_instance
        self.speedometer.server_sshpass.exec_command = Mock(return_value=("output_1", "error_1", 0))
        self.speedometer.client_sshpass.exec_command = Mock(return_value=("output_2", "error_2", 0))
        stdout, stderr, returncode = self.speedometer.exec_iperf()

        self.assertEqual(stdout, "output_2")
        self.assertEqual(stderr, "error_2")
        self.assertEqual(returncode, 0)

        mock_thread.assert_called_once_with(target=self.speedometer.server_sshpass.exec_command, args=("iperf3 -s -1",))
        mock_thread_instance.start.assert_called_once()

    @patch("threading.Thread")
    def test_exec_iperf_with_exception(self, mock_thread):
        mock_thread_instance = Mock()
        mock_thread.return_value = mock_thread_instance
        self.speedometer.server_sshpass.exec_command = Mock(return_value=("output_1", "error_1", 0))
        self.speedometer.client_sshpass.exec_command = Mock(return_value=("output_2", "error_2", 1))

        with self.assertRaises(Exception) as context:
            self.speedometer.exec_iperf()
        self.assertEqual(str(context.exception), "Connection error")

        # Проверяем, что mock_thread был вызван
        mock_thread.assert_called_once_with(target=self.speedometer.server_sshpass.exec_command, args=("iperf3 -s -1",))
        mock_thread_instance.start.assert_called_once()


if __name__ == "__main__":
    unittest.main()
