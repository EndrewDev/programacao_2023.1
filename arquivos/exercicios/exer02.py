def cedula(valor):
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
            totalced = 0
            if total == 0:
                break
    return

saca = float(input('Digite o valor que você quer sacar: '))

x = cedula(saca)

print(x)