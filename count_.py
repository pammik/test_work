import json
file = "hosts.txt"
myfile = open(file, mode='r', encoding='utf-8')
count = 0
d = []
for line in myfile:
    line = line.replace('[', ' ').replace(']', ' ').replace(',', ' ')
    line = line.strip('\n')
    if line != ' ':
        d.append(line)
        count += 1
test = {}
for i in range(count):
    d[i].


