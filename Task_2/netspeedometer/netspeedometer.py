from .sshpass_module import SSHPASSInterface
import subprocess
import threading
import time


class NetSpeedometer(SSHPASSInterface):
    def __init__(self, host, user, password, option, protocol="ssh", bandwidth_tester="iperf3"):
        super().__init__(host, user, password, option, protocol)
        self.bandwidth_tester = bandwidth_tester

    def exec_iperf(self):
        # Запуск iperf3 на сервере
        print("Loading of server...")
        server_thread = threading.Thread(target=self.exec_command, args=(f"{self.bandwidth_tester} -s -1",))
        server_thread.start()
        self.wait_server_loading() # вместо time.sleep(20)

        # Запуск iperf3 на клиенте
        print("Loading of client...")
        client_command = f"{self.bandwidth_tester} -c {self.host} -J"
        client_process = subprocess.Popen(client_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = client_process.communicate()

        return stdout, stderr, client_process.returncode

    def wait_server_loading(self):
        code = -1
        start = time.time()
        while code != 0:
            outs, errs, code = self.exec_command(f"pgrep {self.bandwidth_tester}")
            end = time.time()
            if end - start > 20:
                raise TimeoutError("Server bandwidth tester did not load")

