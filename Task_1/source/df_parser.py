from base_parser import BaseParser

class DFParser(BaseParser):
    def __init__(self, args):
        self.__header = self.__get_header_by_args(args)

    def __get_header_by_args(self, args):
        if args.human:
            return ['Filesystem', 'Size', 'Used', 'Avail', 'Use%', 'Mounted on']
        elif args.inode:
            return ['Filesystem', 'Inodes', 'IUsed', 'IFree', 'IUse%', 'Mounted on']
        else:
            return ['Filesystem', '1K-blocks', 'Used', 'Available', 'Use%', 'Mounted on']
        
    def parse(self, outs):
        lines = outs.split('\n')[1:]
        return [dict(zip(self.__header, line.split())) for line in lines if line]