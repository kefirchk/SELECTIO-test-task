from .sshpass_module import SshpassInterface
from .network_params import NetworkParams
import threading


class NetSpeedometer:
    def __init__(self, net_args, protocol="ssh", bandwidth_tester="iperf3"):
        self.net_params = NetworkParams(net_args)
        self.protocol = protocol
        self.bandwidth_tester = bandwidth_tester
        self.server_sshpass = SshpassInterface(host=self.net_params.server_ip,
                                               user=self.net_params.server_user,
                                               password=self.net_params.server_password,
                                               pass_option=self.net_params.server_pass_option,
                                               protocol=self.protocol)
        self.client_sshpass = SshpassInterface(host=self.net_params.client_ip,
                                               user=self.net_params.client_user,
                                               password=self.net_params.client_password,
                                               pass_option=self.net_params.client_pass_option,
                                               protocol=self.protocol)


    def exec_iperf(self):
        # Запуск iperf3 на сервере
        print("Loading of server...")
        server_command = f"{self.bandwidth_tester} -s -1"
        server_thread = threading.Thread(target=self.server_sshpass.exec_command, args=(server_command,))
        server_thread.start()
        self.server_sshpass.wait_loading(self.bandwidth_tester)

        # Запуск iperf3 на клиенте
        print("Loading of client...")
        client_command = f"{self.bandwidth_tester} -c {self.net_params.server_ip} -J"
        stdout, stderr, returncode = self.client_sshpass.exec_command(client_command)

        if returncode:
            self.server_sshpass.stop_process(self.bandwidth_tester)
            raise Exception("Connection error")

        return stdout, stderr, returncode
