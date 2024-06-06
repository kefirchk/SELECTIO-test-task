import subprocess


class SSHPASSInterface:
    def __init__(self, host, user, password, option='-p', protocol='ssh'):
        self.host = host
        self.user = user
        self.password = password
        self.option = option
        self.protocol = protocol

    def exec_command(self, command):
        full_command = f"sshpass {self.option} {self.password} {self.protocol} {self.user}@{self.host} {command}"
        process = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8'), process.returncode
