# Faça um programa que você digita sua data de nascimento (formato
# dd/mm/aaaa) e ele vai lhe informar quantos dias faltam para o seu
# próximo aniversário

import datetime

# lista_data = []
day = input('Digite sua data nascimento: ')
# lista_data += day
# lista_data = lista_data.split('/')
nasc_endy = datetime.datetime(day)
falta = datetime.datetime.now() - nasc_endy
print(f'Data nascimento: {nasc_endy}')
print(f'Quantas dias faltas para próximo aniversario: {falta.days}')