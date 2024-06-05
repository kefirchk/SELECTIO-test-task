from argument_parser import ArgumentParser
from ssh_interface import SSHInterface

PROTOCOL = "ssh"
HOST = "192.168.0.3"
USER = "alexei"
OPTION = "-p"
PASSWORD = "1234"
COMMAND = "ls"

def main():
    #argparser = ArgumentParser()
    #args = argparser.get_args()
    #print(args.password)
    #print(args.file_name)
    #password = argparser.get_password(args)
    #print(password)

    ssh_interface = SSHInterface(protocol=PROTOCOL, host=HOST, user=USER, password=PASSWORD, option=OPTION)

    stdout, stderr, returncode = ssh_interface.exec_command(COMMAND)
    print('STDOUT:', stdout)
    print('STDERR:', stderr)
    print('Return Code:', returncode)


if __name__ == "__main__":
    main()
