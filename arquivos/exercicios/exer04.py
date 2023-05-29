import datetime

def transforma_datas(data):
    listas_semnas = []
    x = datetime.datetime(data)
    semanas = x.weekday()
    dias = x.day
    anos = x.year
    meses = x.month
    listas_semnas.append({'dias': dias, 'semanas': semanas, 'mês': meses, 'anos': anos})

datas = datetime.datetime(2020, 4, 6)
respostas = transforma_datas(datas)

print(respostas)