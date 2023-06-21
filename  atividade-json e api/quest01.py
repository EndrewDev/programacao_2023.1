import json

with open('apache_logs.txt', 'r') as openfile:
    json_objeto = json.loads(openfile)
    for i in json_objeto:
        print(i)

print(type(json_objeto))