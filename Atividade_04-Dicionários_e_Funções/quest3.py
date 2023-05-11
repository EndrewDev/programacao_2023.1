# def area(calcula):
#     a = calcula * calcula
#     return a

# lado = input('Digite o lado do quadrado:\n')
# area(lado)
# print(f'Area: {area}')

# def peri(calculador):
#     p = calculador * 4
#     return p

def area(larg, comp):
    a = larg * comp
    return f'A área de um terreno {larg}x{comp} e de {a}m².'

l = float(input('Largura:\n'))
c = float(input('Comprimento:\n'))
area(l, c)
print(f'Controle de Terreno {area}.')