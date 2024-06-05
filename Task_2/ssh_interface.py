import subprocess

class SSHInterface:
    def __init__(self, protocol, host, user, password, option):
        self.protocol = protocol
        self.host = host
        self.user = user
        self.password = password
        self.option = option

    def exec_command(self, command):
        #"sshpass -p 1234 ssh alexei@192.168.0.3 ls -l"
        full_command = f"sshpass {self.option} {self.password} {self.protocol} {self.user}@{self.host} command"
        process = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8'), process.returncode