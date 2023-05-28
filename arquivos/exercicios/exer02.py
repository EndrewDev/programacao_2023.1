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
                cedula200 = []
                cedula = 100
                cedula200.append(cedula)
            elif cedula == 100:
                cedula100 = []
                cedula = 50
                cedula100 = cedula
            elif cedula == 50:
                cedula50 = []
                cedula = 20
                cedula50.append(cedula)
            elif cedula == 20:
                cedula20 = []
                cedula = 10
                cedula20.append(20)
            elif cedula == 10:
                cedula10 = []
                cedula = 5
                cedula10.append(cedula)
            elif cedula == 5:
                cedula5 = []
                cedula = 1
            elif cedula == 1:
                cedula1 = []
                cedula = 0
                cedula1.append(cedula)
                cedula5.append(cedula)
            listas_cedulas.append({'valor': valor, '200': cedula200, '100': cedula100, '50': cedula50, '20': cedula20, '10': cedula10, '5': cedula5})
            totalced = 0
            if total == 0:
                break
    return listas_cedulas

lista_cedulas = {}

saca = float(input('Digite o valor que você quer sacar: '))

x = cedula(saca)
# for i in x:
#     lista_cedulas.append(i)
#     print(lista_cedulas)

print(x)