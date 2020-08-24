import paramiko
import time
try:
    a = "192.168.145.101"
    cli = paramiko.client.SSHClient()
    cli.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
    cli.connect(hostname=a, username="pamik01", password="fQAg7MdHc01")
    stdin_, stdout_, stderr_ = cli.exec_command("cd bw/ && svn info --show-item url")
    stdout_.channel.recv_exit_status()
    lines = stdout_.readlines()
    print(lines)
    for line in lines:
        b = line
    stdin_, stdout_, stderr_ = cli.exec_command("cd bw/ && svn info --show-item revision")
    stdout_.channel.recv_exit_status()
    lines = stdout_.readlines()
    for line in lines:
        c = line
    print("Branch: " + b + "Revision: " + c)
    cli.close()
except TimeoutError:
    print("server " + a + " недоступен")