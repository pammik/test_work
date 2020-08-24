import paramiko
import time
import base64
import json

user1 = {
    "vcs_type": "",
    "branch": "",
    "hostname": "192.168.145.101",
    "user": "pamik01",
    "type_auth": "password",
    "key": "fQAg7MdHc01"
}
user2 = {
    "vcs_type": "",
    "branch": "",
    "hostname": "",
    "user": "user2",
    "type_auth": "key"
}
user3 = {
    "vcs_type": "",
    "branch": "",
    "hostname": "",
    "user": "user3",
    "type_auth": "key"
}
cli = paramiko.client.SSHClient()
cli.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())

    cli.connect(hostname=user1["hostname"], username=user1["user"], password=user1["key"])
    stdin_, stdout_, stderr_ = cli.exec_command("cd bw/ && git rev-parse --abbrev-ref HEAD")
    stdout_.channel.recv_exit_status()
    lines = stdout_.readlines()
    for line in lines:
        b = line
    stdin_, stdout_, stderr_ = cli.exec_command("cd bw/ && git rev-list --count HEAD")
    stdout_.channel.recv_exit_status()
    lines = stdout_.readlines()
    for line in lines:
        c = line
    print("Branch: " + b + "Revision: " + c)
    cli.close()
print(user1)

output_json = []
output_json.append(user1)
output_json.append(user2)
output_json.append(user3)

file = 'result'
myfile = open(file, mode= 'w', encoding='utf-8')

json.dump(output_json, myfile)
