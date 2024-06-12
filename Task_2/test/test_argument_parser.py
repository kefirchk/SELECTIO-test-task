import unittest
from unittest.mock import patch, Mock
from Task_2.netspeedometer.parser_module.argument_parser import ArgumentParser


class TestArgumentParser(unittest.TestCase):
    @patch('argparse.ArgumentParser.parse_args')
    def test_get_args(self, mock_args):
        mock_args.return_value = Mock(server_password='1234',
                                      server_pass_file_name=None,
                                      client_password='5678',
                                      client_pass_file_name=None,
                                      server_user='alex',
                                      client_user='bob',
                                      server_ip='192.168.0.3',
                                      client_ip='192.168.0.4')
        args = ArgumentParser.get_args()
        self.assertEqual(args.server_password, '1234')
        self.assertIsNone(args.server_pass_file_name)
        self.assertEqual(args.client_password, '5678')
        self.assertIsNone(args.client_pass_file_name)
        self.assertEqual(args.server_user, 'alex')
        self.assertEqual(args.client_user, 'bob')
        self.assertEqual(args.server_ip, '192.168.0.3')
        self.assertEqual(args.client_ip, '192.168.0.4')


if __name__ == '__main__':
    unittest.main()
