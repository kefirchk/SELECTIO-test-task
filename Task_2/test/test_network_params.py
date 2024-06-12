import unittest
from Task_2.netspeedometer import NetworkParams
from unittest.mock import Mock


class TestNetworkParams(unittest.TestCase):
    def test_get_password(self):
        net_args = Mock(client_ip="192.168.1.10",
                        server_ip="192.168.1.20",
                        client_user="user1",
                        server_user="user2",
                        server_password="secret",
                        server_pass_file_name=None,
                        client_password=None,
                        client_pass_file_name="file.txt")
        instance = NetworkParams(net_args)
        self.assertEqual(instance.server_password, "secret")
        self.assertEqual(instance.server_pass_option, "-p")
        self.assertEqual(instance.client_password, "file.txt")
        self.assertEqual(instance.client_pass_option, "-f")


if __name__ == "__main__":
    unittest.main()
