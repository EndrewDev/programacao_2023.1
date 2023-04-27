registro = []

while True:
    print('Para sair digite "SAIR" a qualquer momento')
    nome = input('Digite o nome:\n')
    if nome == 'SAIR' or nome == 'sair':
        break
    idade = input('Digite idade:\n')
    if idade == 'SAIR' or idade == 'sair':
        break
    registro.append({'nome': nome, 'idade': idade})

soma = 0
for pessoas in registro:
    pessoas = pessoas(pessoas['idade'])
    soma = soma + pessoas['idade']

media = pessoas / len(pessoas)

print(media)