import datetime
import pickle
# import calendar

# print(calendar.month(2020, 4))

def transforma_datas(data):
    listas_datas = []
    for i in data:
        listas_datas.append(i)
    data = datetime.datetime(listas_datas)
    for seamana in data:
        if seamana == data.weekday(6):
            print(f"Quantas tem os dias dos seamana: {data}")
    return

datas = datetime.date(2020, 4, 5)

respostas = transforma_datas(datas)

print(respostas)