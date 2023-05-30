from datetime import date
import pickle
import calendar

# print(calendar.month(2020, 4))

def transforma_datas(datainicio):
    comeca = date(datainicio)
    listas_semanas = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quieIra-feira', 'sexta-feira', 'sábado', 'domingo']
    seegundas = []
    tercas = []
    quartas = []
    quintas = []
    sextas = []
    sabados = []
    domingos = []
    if listas_semanas[0] == comeca.weekday(0):
        seegundas.append(comeca.weekday(0))
    elif listas_semanas[1] == comeca.weekday(1):
        tercas.append(comeca.weekday(1))
    elif listas_semanas[2] == comeca.weekday(2):
        quartas.append(comeca.weekday(2))
    elif listas_semanas[3] == comeca.weekday(3):
        quintas.append(comeca.weekday(3))
    elif
    final = print(f'Tens qunatas dias de semanas: {dias}')
    return final

data_comeca = date(2020, 4, 5)

respostas = transforma_datas(data_comeca)
print(respostas)

with open('data.pick.txt', 'wb') as f:
    dado = pickle.load(respostas, f)