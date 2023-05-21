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
    pessoas.append([nome, peso, altura, imc])

cadastradas = len(pessoas)
print(f"Quantas pessoas foram cadastradas: {cadastradas}")

def segunda_peso(items):
    return items[1]

lista_peso = sorted(pessoas, key=segunda_peso)

print(lista_peso)

def terceiro_peso(items):
    return items[2]

lista_peso = sorted(pessoas, key=terceiro_peso)

print(lista_peso)

def segunda_imc(items):
    return items[3]

lista_imc = sorted(pessoas, key=segunda_imc)

print(lista_imc)


def terceiro_imc(items):
    return items[3]

lista_imc = sorted(pessoas, key=terceiro_imc)

print(lista_imc)