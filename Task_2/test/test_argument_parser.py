import unittest
from unittest.mock import patch, Mock
from Task_2.netspeedometer.parser_module.argument_parser import ArgumentParser

class TestArgumentParser(unittest.TestCase):
    def setUp(self):
        self.parser = ArgumentParser()

    def test_get_password_with_file(self):
        args = Mock()
        args.file_name = 'password.txt'
        args.password = None

        password, option = self.parser.get_password(args)

        self.assertEqual(password, 'password.txt')
        self.assertEqual(option, '-f')

    def test_get_password_with_password(self):
        args = Mock()
        args.file_name = None
        args.password = 'pass123'

        password, option = self.parser.get_password(args)

        self.assertEqual(password, 'pass123')
        self.assertEqual(option, '-p')

    @patch('argparse.ArgumentParser.parse_args')
    def test_get_args(self, mock_args):
        mock_args.return_value = Mock(password='1234', file_name=None, user='user', host='test.com')
        args = self.parser.get_args()
        self.assertEqual(args.password, '1234')
        self.assertEqual(args.file_name, None)
        self.assertEqual(args.user, 'user')
        self.assertEqual(args.host, 'test.com')

if __name__ == '__main__':
    unittest.main()
