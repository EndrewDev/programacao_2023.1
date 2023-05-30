import datetime
import pickle
# import calendar

# print(calendar.month(2020, 4))

def transforma_datas(data):
    listas_datas = []
    listas_datas.append(data)
    data = datetime.datetime(listas_datas)
    for i in data:
        if i == data.weekday(6):
            print(i)
    return

datas = datetime.date(2020, 4, 5)

respostas = transforma_datas(datas)

print(respostas)