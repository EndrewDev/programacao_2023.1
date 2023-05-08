numericos = []
maior = 0
menor = 0

print('Digite "FIM" para parar de digite qulaquer momento')
while True:
    valor = input('Digite qualquer valor:\n')
    if valor == 'Fim' or valor == 'FIM' or valor == 'fim':
        break
    lista_numericos = int(valor)
    numericos.append(lista_numericos)

print(numericos)