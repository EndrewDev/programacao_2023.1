pessoas = []

print('Se quiser para de digite apena digite "FIM"')
def IMC(pessoa):
    while True:
        nome = input('Digite seu nome:\n')
        peso = int(input('Digite seu peso:\n'))
        altura = float(input('Digite a sua altura:\n'))
        if nome == "FIM" or nome == 'Fim' or nome == 'fim':
            break
        if peso == 'FIM' or peso == 'Fim' or peso == 'fim':
            break
        if altura == 'FIM' or altura == 'Fim' or altura == 'fim':
            break
        pessoas.append({'nome': nome, 'peso': peso, 'altura': altura})
    
    imc = peso / altura**2
    return f'O {nome} seu IMC é {imc}'

print(IMC)