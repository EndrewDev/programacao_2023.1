import json

# dados = {}

# for i in range(dados):
#     i = json.dumps(i)
#     print(i)

# print(dados1)

with open('apach_logs.json', 'r') as openfile:
    json_objeto = json.load(openfile)

print(json_objeto)
print(type(json_objeto))