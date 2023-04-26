meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'jumho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

data_str = input('Digite a data no formato "dd/mm/aaaa":\n')

data = data_str.split('/')

print(f'{data[0]} de {meses[int(data[1]) - 1]} de {data[2]}')