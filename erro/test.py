lista_numericos = []
for _ in range(5):
    while(True):
        try:
            x = input('Digite im valor: ')
            lista_numericos.append(x)
            break
        except ValueError as e:
            print('Você deve digitar somente os númerio inteiro.')
lista_ord = sorted(lista_numericos)
menor = lista_numericos[0]
maior = lista_numericos[-1]

print(f'O maior valor é {maior} e sua posição na lista é {lista_numericos.index}')
print(f'O menor valor é {menor} s sua posição na lista é {lista_numericos.index}')