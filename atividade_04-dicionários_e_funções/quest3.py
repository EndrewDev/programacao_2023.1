def area(larg, comp):
    a = larg * comp
    p = c * 4
    return a, p

l = float(input('Largura:\n'))
c = float(input('Comprimento:\n'))
peri = float(input('Digite o valor de perímetro:\n'))
area(l, c)
print(f'Controle de Terreno {area(l, c)}.')
