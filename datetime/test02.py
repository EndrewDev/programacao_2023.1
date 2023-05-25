# Faça um programa que você digita sua data de nascimento (formato
# dd/mm/aaaa) e ele vai lhe informar quantos dias faltam para o seu
# próximo aniversário

import datetime

lista_data = []

day = input('Digite a data no formato "dd/mm/aaaa":\n')
lista_data = day.split('/')
# lista_data = lista_data.join(lista_data)
# print(lista_data)

nasc_endy = datetime.datetime(lista_data)
falta = datetime.datetime.now() - nasc_endy
print(f'Data nascimento: {nasc_endy}')
print(f'Quantas dias faltas para próximo aniversario: {falta.days}')