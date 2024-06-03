import unittest
from unittest.mock import Mock, patch
from main import main, get_args
import json

class TestMain(unittest.TestCase):
    @patch('argparse.ArgumentParser.parse_args')
    def test_get_args(self, mock_args):
        mock_args.return_value = Mock(human=False, inode=True)
        args = get_args()
        self.assertFalse(args.human)
        self.assertTrue(args.inode)

    @patch('main.get_args')
    @patch('source.DFExecuter.execute')
    def test_main_success(self, mock_execute, mock_get_args):
        mock_get_args.return_value = Mock(human=False, inode=False)
        mock_execute.return_value = "is_test"
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with(
                json.dumps({"status": "success", "error": "None", "result": "is_test"}, indent=4))


    @patch('main.get_args')
    @patch('source.DFExecuter.execute')
    def test_exception_handling(self, mock_execute, mock_get_args):
        mock_get_args.return_value = Mock(human=False, inode=False)
        mock_execute.side_effect = Exception("Something went wrong")
        with patch('builtins.print') as mock_print:
            main()
            #self.assertRaises(Exception, main)
            mock_print.assert_called_with(
                json.dumps({"status": "failure", "error": "Something went wrong", "result": "None"}, indent=4))
