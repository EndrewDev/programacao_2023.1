# def peri(c):
#     p = c * 4
#     return p
# perim = float('Digite o valor de perimentro:\n')
# peri(perim)
# print(f'Perimentro: {peri}')

def area(larg, comp, c):
    a = larg * comp
    p = c * 4
    return a, p

l = float(input('Largura:\n'))
co = float(input('Comprimento:\n'))
peri = float(input('Digite o valor de perímetro:\n'))
print(f'Controle de Terreno {area(l, co)}.\n O controler de perímetro: {area(peri)}')