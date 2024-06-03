import unittest
from unittest.mock import Mock, patch
from source import DFExecuter

class TestDFExecuter(unittest.TestCase):
    def test_get_options_by_args_human(self):
        args = Mock()
        args.human = True
        args.inode = False
        executer = DFExecuter(args)
        self.assertEqual(executer._DFExecuter__get_options_by_args(args), ['df', '-h'])

    def test_get_options_by_args(self):
        args = Mock()
        args.human = False
        args.inode = True
        executer = DFExecuter(args)
        self.assertEqual(executer._DFExecuter__get_options_by_args(args), ['df', '-i'])

    @patch('subprocess.Popen')
    @patch('source.df_parser.DFParser')
    def test_execute(self, mock_parser, mock_popen):
        args = Mock()
        args.human = False
        args.inode = False
        executer = DFExecuter(args)
        executer._DFExecuter__options = ['df']
        mock_process = Mock()
        mock_process.communicate.return_value = (b'Filesystem 1K-blocks Used Available Use% Mounted on\n/dev/sda1 123456 12345 100000 12% /\n', b'')
        mock_popen.return_value = mock_process
        mock_parser.return_value.parse.return_value = [{'Filesystem': '/dev/sda1', '1K-blocks': '123456', 'Used': '12345', 'Available': '100000', 'Use%': '12%', 'Mounted on': '/'}]
        result = executer.execute()
        self.assertEqual(result, [{'Filesystem': '/dev/sda1', '1K-blocks': '123456', 'Used': '12345', 'Available': '100000', 'Use%': '12%', 'Mounted on': '/'}])

    @patch('subprocess.Popen')
    @patch('source.df_parser.DFParser')
    def test_execute_exception(self, mock_parser, mock_popen):
        args = Mock()
        args.human = False
        args.inode = False
        executer = DFExecuter(args)
        executer._DFExecuter__options = ['df']
        mock_process = Mock()
        mock_process.communicate.return_value = ('', 'Some error!')
        mock_popen.return_value = mock_process
        mock_parser.return_value.parse.return_value = [
            {'Filesystem': '/dev/sda1', '1K-blocks': '123456', 'Used': '12345', 'Available': '100000', 'Use%': '12%',
             'Mounted on': '/'}]
        self.assertRaises(Exception, executer.execute)
