pessoas = []

print('Se quiser para de digite apena digite "FIM"')
while True:
    nome = input('Digite seu nome:\n')
    if nome == "FIM" or nome == 'Fim' or nome == 'fim':
        break
    peso = int(input('Digite seu peso:\n'))
    if peso == 'FIM' or peso == 'Fim' or peso == 'fim':
        break
    altura = float(input('Digite a sua altura:\n'))
    if altura == 'FIM' or altura == 'Fim' or altura == 'fim':
        break
    imc = peso/(altura)**2
    pessoas.append({'nome': nome, 'peso': peso, 'altura': altura, 'imc': imc})

print(pessoas)