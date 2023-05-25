# Faça um programa que você digita sua data de nascimento (formato
# dd/mm/aaaa) e ele vai lhe informar quantos dias faltam para o seu
# próximo aniversário

import datetime

data_nasc = []
day = input('Digite seu nascimento formato dd/mm/aaaa: ')
data_nasc = day.split('/')

nasc_endy = datetime.date(data_nasc)
falta = datetime.datetime.now() - nasc_endy
print(f'Data nascimento: {nasc_endy}')
print(f'Quantas dias faltas para próximo aniversario: {falta}')