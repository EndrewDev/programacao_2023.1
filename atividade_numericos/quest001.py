nota1 = float(input("Digite a nota primeira:\n"))
nota2 = float(input('Digite a nota segunda:\n'))
media = nota1 + nota2 / 2
if media >= 7.0:
    print(f"A média {media} foi aprovado.")
elif media < 2.0:
    print(f'A média {media} foi reprovado.')
else:
    if 2.0 <= media and media < 7.0:
        print(f'A média {media} foi recuperaçõa.')