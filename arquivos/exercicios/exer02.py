def cedula(valor):
    listas_cedulas = []
    total = valor
    cedula = 200
    totalced = 0
    while True:
        if total >= cedula:
            total -= cedula
            totalced += 1
        else:
            print(f'Total {totalced} cédulas de R$: {cedula} ')
            if cedula == 200:
                cedula = 100
            elif cedula == 100:
                cedula = 50
            elif cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 5
            elif cedula == 5:
                cedula = 1
            elif cedula == 1:
                cedula = 0
            listas_cedulas.append({'valor': valor, '200': listas_cedulas[0], '100': listas_cedulas[1], '50': listas_cedulas[2], '20': listas_cedulas[3], '10': listas_cedulas[4], '5': listas_cedulas[5], '1': listas_cedulas[6]})
            totalced = 0
            if total == 0:
                break
    return listas_cedulas

saca = float(input('Digite o valor que você quer sacar: '))

x = cedula(saca)
# for i in x:
#     lista_cedulas.append(i)
#     print(lista_cedulas)

print(x)