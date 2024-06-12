class NetworkParams:
    def __init__(self, net_args):
        self.client_ip = net_args.client_ip
        self.server_ip = net_args.server_ip
        self.client_user = net_args.client_user
        self.server_user = net_args.server_user
        self.server_password, self.server_pass_option = self.get_password(net_args.server_password, net_args.server_pass_file_name)
        self.client_password, self.client_pass_option = self.get_password(net_args.client_password, net_args.client_pass_file_name)

    def get_password(self, password: str, filename: str):
        if password is not None:
            return password, '-p'
        else:
            return filename, '-f'

