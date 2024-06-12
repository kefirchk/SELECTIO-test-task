import subprocess
import time
from typing import Tuple


class SshpassInterface:
    def __init__(self, host: str, user: str, password: str, pass_option: str, protocol: str = 'ssh'):
        self.host = host
        self.user = user
        self.password = password
        self.pass_option = pass_option
        self.protocol = protocol
        self.process = None

    def exec_command(self, command: str) -> Tuple[str, str, int]:
        full_command = f"sshpass {self.pass_option} {self.password} {self.protocol} {self.user}@{self.host} {command}"
        self.process = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = self.process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8'), self.process.returncode

    def wait_loading(self, bandwidth_tester):
        code = -1
        start = time.time()
        while code != 0:
            outs, errs, code = self.exec_command(f"pgrep {bandwidth_tester}")
            end = time.time()
            if end - start > 20:
                break
            time.sleep(1)

    def stop_process(self, bandwidth_tester):
        if self.process:
            self.exec_command(f"pkill {bandwidth_tester}")
