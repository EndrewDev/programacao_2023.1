from datetime import date
import pickle
# import calendar

# print(calendar.month(2020, 4))

def transforma_datas(data):
    x = date(data).isocalendar()
    final = print(f'Quantas tens os dias de semanas: {x}')
    return final

datas = date(2020, 4, 4)

respostas = transforma_datas(datas)

print(respostas)

with open('data.pick.txt', 'wb') as f:
    dado = pickle.load(respostas, f)