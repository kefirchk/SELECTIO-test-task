# ФАЙЛ ДЛЯ ТЕСТИРОВАНИЯ МОДУЛЯ

from sshpass_interface import SSHPASSInterface


PROTOCOL = "ssh"
HOST = "192.168.0.3"
USER = "alexei"
OPTION = "-f"
PASSWORD = "./test/file.txt"
COMMAND = "ls"

def main():
    ssh_interface = SSHPASSInterface(protocol=PROTOCOL, host=HOST, user=USER, password=PASSWORD, option=OPTION)
    stdout, stderr, returncode = ssh_interface.exec_command(COMMAND)
    print('STDOUT:', stdout)
    print('STDERR:', stderr)
    print('Return Code:', returncode)

if __name__ == "__main__":
    main()
