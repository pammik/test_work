import paramiko
import time
a = "172.17.54.108"
cli = paramiko.client.SSHClient()
cli.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
cli.connect(hostname=a, username="pamik01", password="fQAg7MdHc01")
stdin_, stdout_, stderr_ = cli.exec_command("cd bw/ && ls -lh")
# time.sleep(2)    # Previously, I had to sleep for some time.
stdout_.channel.recv_exit_status()
lines = stdout_.readlines()
for line in lines:
    print(line)
cli.close()