import unittest
from unittest.mock import Mock
from source import DFParser


class TestDFParser(unittest.TestCase):
    def test_get_header_by_args_human(self):
        args = Mock()
        args.human = True
        args.inode = False
        parser = DFParser(args)
        self.assertEqual(parser._DFParser__get_header_by_args(args),
                         ['Filesystem', 'Size', 'Used', 'Avail', 'Use%', 'Mounted on'])

    def test_get_header_by_args_inode(self):
        args = Mock()
        args.human = False
        args.inode = True
        parser = DFParser(args)
        self.assertEqual(parser._DFParser__get_header_by_args(args),
                         ['Filesystem', 'Inodes', 'IUsed', 'IFree', 'IUse%', 'Mounted on'])

    def test_get_header_by_args_empty(self):
        args = Mock()
        args.inode = False
        args.human = False
        parser = DFParser(args)
        self.assertEqual(parser._DFParser__get_header_by_args(args),
                         ['Filesystem', '1K-blocks', 'Used', 'Available', 'Use%', 'Mounted on'])

    def test_parse(self):
        args = Mock()
        args.human = True
        parser = DFParser(args)
        parser._DFParser__header = ['Filesystem', '1K-blocks', 'Used', 'Available', 'Use%', 'Mounted on']
        outs = "Filesystem 1K-blocks Used Available Use% Mounted on\n/dev/sda1 123456 12345 100000 12% /\n"
        result = parser.parse(outs)
        self.assertEqual(result, [
            {'Filesystem': '/dev/sda1', '1K-blocks': '123456', 'Used': '12345', 'Available': '100000', 'Use%': '12%',
             'Mounted on': '/'}])
