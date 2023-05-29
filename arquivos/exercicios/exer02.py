import pickle

def cedula(valor):
    listas_cedulas = []
    total = int(valor)
    cedula = 200
    totalced = 0
    doiscento = 0
    cem = 0
    cinqueta = 0
    vinte = 0
    dez = 0
    cinco = 0
    um = 0
    while True:
        if total >= cedula:
            total -= cedula
            totalced += 1
        else:
            print(f'Total {totalced} cédulas de R$: {cedula} ')
            if cedula == 200:
                doiscento += 1
                cedula = 100
            elif cedula == 100:
                cem += 1
                cedula = 50
            elif cedula == 50:
                cinqueta += 1 
                cedula = 20
            elif cedula == 20:
                vinte += 1
                cedula = 10
            elif cedula == 10:
                dez += 1
                cedula = 5
            elif cedula == 5:
                cinco += 1
                cedula = 1
            elif cedula == 1:
                cedula = 0
            totalced = 0
            if total == 0:
                break
    listas_cedulas.append({'200': doiscento, '100': cem, '50': cinqueta, '10': dez, '5': cinco, '1': um})
    respostas = print(f'{listas_cedulas}')
    return

saca = float(input('Digite o valor que você quer sacar: '))

print(cedula(saca))