import paramiko
import time
import base64
import json
import getpass
import os.path

user1 = {
    "user": "pamik",
    "hostname": "192.168.1.48",
    "auth_type": "",
    "password": "fQAg7MdHc01" # Временный ключ
}
def_acc = getpass.getuser()
con_serv = paramiko.client.SSHClient()
con_serv.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
chck_file = os.path.exists("/home/" + str(def_acc) + "/.ssh/id_rsa")
if chck_file:
    user1.update({"auth_type": "key"})
    key = paramiko.RSAKey.from_private_key_file("/home/" + str(def_acc) + "/.ssh/id_rsa")
    con_serv.connect(hostname=user1["hostname"], username=user1["user"], pkey=key)
    stdin_, stdout_, stderr_ = con_serv.exec_command("cd /bw/test_work && git ver-parse --abbrev-ref HEAD")
    stdout_.channel.recv_exit_status()
    lines = stdout_.readlines()[0].rstrip()
    if lines != "":
        user1.update({"vcs_type": "git"})
        user1.update({"branch": lines})
        stdin_, stdout_, stderr_ = con_serv.exec_command("cd bw/test_work && git rev-list --count HEAD")
        stdout_.channel.recv_exit_status()
        lines = stdout_.readlines()[0].rstrip()
        user1.update({"revision": lines})
    else:
        user1.update({"vcs_type": "svn"})
        stdin_, stdout_, stderr_ = con_serv.exec_command("cd bw/test_work/ && svn info --show-item url")
        stdout_.channel.recv_exit_status()
        lines = stdout_.readlines()[0].rstrip()
        user1.update({"branch": lines})
        stdin_, stdout_, stderr_ = con_serv.exec_command("cd bw/test_work && svn info --show-item revision")
        stdout_.channel.recv_exit_status()
        lines = stdout_.readlines()[0].rstrip()
        user1.update({"revision": lines})
    con_serv.close()
else:
    user1.update({"auth_type": "password"})
    con_serv.connect(hostname=user1["hostname"], username=user1["user"], password=user1["password"])
    stdin_, stdout_, stderr_ = con_serv.exec_command("cd bw/test_work/ && git rev-parse --abbrev-ref HEAD")
    stdout_.channel.recv_exit_status()
    lines = stdout_.readlines()[0].rstrip()
    if lines != "":
        user1.update({"vcs_type": "git"})
        user1.update({"branch": lines})
        stdin_, stdout_, stderr_ = con_serv.exec_command("cd bw/test_work && git rev-list --count HEAD")
        stdout_.channel.recv_exit_status()
        lines = stdout_.readlines()[0].rstrip()
        user1.update({"revision": lines})
    else:
        user1.update({"vcs_type": "svn"})
        stdin_, stdout_, stderr_ = con_serv.exec_command("cd bw/test_work/ && svn info --show-item url")
        stdout_.channel.recv_exit_status()
        lines = stdout_.readlines()[0].rstrip()
        user1.update({"branch": lines})
        stdin_, stdout_, stderr_ = con_serv.exec_command("cd bw/test_work && svn info --show-item revision")
        stdout_.channel.recv_exit_status()
        lines = stdout_.readlines()[0].rstrip()
        user1.update({"revision": lines})
    con_serv.close()
print(user1)

out_file = open("json_out", mode="w", encoding="utf-8")
json.dump(user1, out_file)