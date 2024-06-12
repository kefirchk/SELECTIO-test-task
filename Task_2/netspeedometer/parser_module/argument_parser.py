import argparse


class ArgumentParser:
    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description='Description of utility')

        s_group = parser.add_mutually_exclusive_group(required=True)
        s_group.add_argument('--s_p', dest='server_password', help='server password')
        s_group.add_argument('--s_f', dest='server_pass_file_name', help='server file name with password')

        c_group = parser.add_mutually_exclusive_group(required=True)
        c_group.add_argument('--c_p', dest='client_password', help='client password')
        c_group.add_argument('--c_f', dest='client_pass_file_name', help='client file name with password')

        parser.add_argument("--s_u", dest='server_user', help="user name", required=True)
        parser.add_argument("--c_u", dest='client_user', help="user name", required=True)
        parser.add_argument("--s_i", dest='server_ip', help="server ip address", required=True)
        parser.add_argument("--c_i", dest='client_ip', help="client ip address", required=True)

        return parser.parse_args()
