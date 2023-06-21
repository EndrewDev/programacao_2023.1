import json

openfile = open('apache_logs.txt', 'tw')
dic_dados = {}

with open(openfile) as f:
    for i in f:
        i, description = i.strip().split(None, 1)
