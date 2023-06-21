import json

openfile = open('apache_logs.txt', 'tw')
dic_dados = {}

with open(openfile) as f:
    for i in f:
        i,description = i.strip().split(None, 1)
dic_dados[i] = description.strip()
outro_file = open('teste1.json', 'w')
json.dump(dic_dados, outro_file, indent= 4, sort_keys=False)
outro_file.close()