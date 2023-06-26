import json, httpx, datetime

lista = []
dic_cotacao = {}

def cotacao():
    data = input('Digite a data para receber o documetno da cotação (formatada aaaa-mm-dd): ')
    lista.append(data.split('-'))
    requisicao = httpx.get('https://economia.awesomeapi.com.br/all/USD-BRL/')
    cotacoa = requisicao.json()

    for i,v in cotacoa.items():
        if cotacao['USD']['create_date'] != data:
            data1 = datetime.datetime(lista[0], lista[1], lista[2])
            cotacao = dict.pop(cotacao['USD']['create_date'])
            cotacao = cotacao['USD']['create_date'] = data1
            print('{}:{}'.format(i, v))
        else:
            if cotacao == data:
                print('{}:{}'.format(i, v))
                
    return cotacoa

cotacao()