from datetime import date
import pickle
import calendar

# print(calendar.month(2020, 4))

def transforma_datas(datainicio):
    comeca = date(datainicio)
    domingos = []
    while True:
        if comeca.weekday(6) == comeca.days():
            domingos.append(comeca.days())
        else:
            break
    final = print(f'Tens qunatas dias de semanas: {domingos}')
    return final

data_comeca = date(2020, 4, 5)

respostas = transforma_datas(data_comeca)
print(respostas)

with open('data.pick.txt', 'wb') as f:
    dado = pickle.load(respostas, f)
