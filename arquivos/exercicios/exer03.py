import json

listas_pessoas = []

while True:
    print("Quer sair digite 'SAIR'")
    nome = input('Digite seu nome: ').strip()
    if nome == 'SAIR' or nome == 'sair':
        break
    sobrenome = input('Digite seu sobrenome: ').strip()
    if sobrenome == 'SAIR' or sobrenome == 'sair':
        break
    idade = int(input('Digite sua idade: ').strip())
    if idade == 'SAIR' or idade == 'sair':
        break
    altura = float(input('Digite seu altura: ').strip())
    if altura == 'SAIR' or altura == 'sair':
        break
    idade = int(idade)
    altura = float(altura)
    listas_pessoas.append({'nome': nome, 'sobrenome': sobrenome, 'idade': idade, 'altura': altura})
    respostas = listas_pessoas

for i in respostas:
    print(i)

with open('contatos.json', 'w') as f:
    contatos = json.load(listas_pessoas, f)