from .df_parser import DFParser
import subprocess

class DFExecuter:
    def __init__(self, args):
        self.__options = self.__get_options_by_args(args)
        self.__parser = DFParser(args)

    def __get_options_by_args(self, args):
        if args.human:
            return ['df', '-h']
        elif args.inode:
            return ['df', '-i']
        else:
            return ['df']
    
    def execute(self):
        process = subprocess.Popen(args=self.__options, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        outs, errs = process.communicate()

        if errs:
            raise Exception(errs.decode('utf-8'))

        return self.__parser.parse(outs.decode('utf-8'))