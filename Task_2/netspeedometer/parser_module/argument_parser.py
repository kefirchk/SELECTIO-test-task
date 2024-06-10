import argparse

class ArgumentParser:
    def get_args(self):
        parser = argparse.ArgumentParser(description='Description of utility')
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--pass', dest='password', help='password')
        group.add_argument('--file', dest='file_name', help='file name with password')

        parser.add_argument("--user", dest='user', help="user name", required=True)
        parser.add_argument("--host", dest='host', help="host (ip address)", required=True)

        return parser.parse_args()

    def get_password(self, args):
        if args.file_name is not None:
            return args.file_name, '-f'
        else:
            return args.password, '-p'
