from datetime import date
import pickle
# import calendar

# print(calendar.month(2020, 4))

def transforma_datas(datainicio, datafinal):
    comeca = date(datainicio).isocalendar()
    final = date(datafinal).isocalendar()
    return f'Tens quantas dais dos domingos: {comeca} e {final}'

data_comeca = date(2020, 4, 6)
data_final = date(2020, 4, 6)

respostas = transforma_datas(data_comeca, data_final)

print(respostas)

with open('data.pick.txt', 'wb') as f:
    dado = pickle.load(respostas, f)