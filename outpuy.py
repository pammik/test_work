import json

filename = "json_temp.txt"
myfile = open(filename, mode = 'w', encoding = 'utf-8')
pr = []
user1 = {
    "vcs_type": "git",
    "branch": "master",
    "revivsion": "3",
    "auth_type": "pass",
    "hostname": "vm1"
}
user2 = {
    "vcs_type": "git",
    "branch": "master",
    "revivsion": "5",
    "auth_type": "key",
    "hostname": "vm2"
}

print(user1["vcs_type"])
pr.append(user1)
pr.append(user2)

##json.dump(pr, myfile)