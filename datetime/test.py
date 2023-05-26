# Faça um programa que você digita sua data de nascimento (formato
# dd/mm/aaaa) e ele vai lhe informar quantos dias faltam para o seu
# próximo aniversário
from datetime import date, timedelta

nasc = input('Digite seu nascimento formato dd/mm/aaaa: ')

hj = date.today()

niver_list = [int(items) for items in nasc.split('/')]

niver_ano_ataul = date(hj.year,niver_list[1], niver_list[0])

if niver_ano_ataul >= hj:
    dias_para_niver = niver_ano_ataul - hj
else:
    dias_para_niver = niver_ano_ataul + timedelta(days=365) - hj
    
# niver = dias_para_niver.strftime('%d')

print(f'Faltam {dias_para_niver} para o seu aniversário!')