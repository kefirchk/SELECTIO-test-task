import argparse

class ArgumentParser:
    def get_args(self):
        parser = argparse.ArgumentParser(description='Description of module for SSHPASS')
        group = parser.add_mutually_exclusive_group()
        group.add_argument('-p', '--password', dest='password', help='password')
        group.add_argument('-f', '--file_name', dest='file_name', help='file name with password')
        return parser.parse_args()
    
    def get_password(args):
        if args.password is not None:
            return args.password
        elif args.file_name is not None:
            with open(args.file_name, 'r') as file:
                password = file.readline()
                return password