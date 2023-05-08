numericos = []

print('Digite "FIM" para parar de digite qulaquer momento')
while True:
    valor = input('Digite qualquer valor:\n')
    if valor == 'Fim' or valor == 'FIM' or valor == 'fim':
        break
    lista_numericos = int(valor)
    numericos.append(lista_numericos)

maior = max(numericos)
menor = min(numericos)

print(f'O valor maior digitado foi:{maior}')
print(f'O valor menor digitado foi:{menor}')

for i in numericos:
    i = i

conta = len(numericos)

media = i / conta
print(f'A média foi: {media}')