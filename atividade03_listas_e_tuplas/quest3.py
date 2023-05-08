valores = []
pares = []
impares = []

print("Ser quiser para de digitir apena digite 'FIM'")
while True:
    numericos = input('Digite qualquer valor:\n')
    if numericos == "FIM" or numericos == "Fim" or numericos == "fim":
        break

    valores.append(int(numericos))
for i in valores:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f'Todos os valores: {valores}')
print(f'A lista de pares:{pares}')
print(f'A lista de impares:{impares}')