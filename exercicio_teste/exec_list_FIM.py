numeros = []

while True:
    valor = input('Digite um valor ou "Fim" para terminar:\n')
    if valor == 'FIM' or valor == 'fim':
        break
    valor_numericos = int(valor)
    numeros.append(valor_numericos)
print(numeros)