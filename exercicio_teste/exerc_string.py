entrada = input('Entre os coeficientes A, B ,C por virgula:\n ')

coef = entrada.split(',')
coef2 = []

for i in coef:
    coef2.append(int(i))

var_a = coef2[0]
var_b = coef2[1]
var_c = coef[2]

delta = var_b**2 - 4*var_a*var_c

x1 = (-var_b + delta**0.5)/2*var_a
x2 = (-var_b - delta**0.5)/2*var_a

eq_formata = f'{var_a}X² + {var_b}X + {var_c}'

print(f'As raizes de equação {eq_formata} são:\n')