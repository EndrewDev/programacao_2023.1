while True:
    listas_pessoas = []
    print("Quer sair digite 'SAIR'")
    nome = input('Digite seu nome: ')
    if nome == 'SAIR' or nome == 'sair':
        break
    sobrenome = input('Digite seu sobrenome: ')
    if sobrenome == 'SAIR' or sobrenome == 'sair':
        break
    idade = int(input('Digite sua idade: '))
    if idade == 'SAIR' or idade == 'sair':
        break
    altura = float(input('Digite seu altura: '))
    if altura == 'SAIR' or altura == 'sair':
        break
    listas_pessoas.append(nome, sobrenome, idade, altura)
    respostas = listas_pessoas

for i in respostas:
    print(i)