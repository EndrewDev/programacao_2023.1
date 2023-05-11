# def fatorial(fato):
#     f = 1
#     while fato > 0:
#         print(f'{fato}', end='')
#         print(f' x ' if fato > 1 else ' = ', end='')
#         f *= fato
#         fato -= 1
#     return f'{f}'

# n = int(input('Digite o valor\n'))
# fatorial(n)
# print(fatorial)

def main():
    n = int(input("Digite o valor de n:\n"))
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    print(f"O valor de {n} eh = {fat}")
main()