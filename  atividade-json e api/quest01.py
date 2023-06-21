import json

openfile = open('apache_logs.txt', 'rt')
openfile.close()
print(openfile)

# with open('apache_logs.txt', 'rt') as openfile:
#     json_objeto = json.loads(openfile)
#     for i in json_objeto:
#         print(i)