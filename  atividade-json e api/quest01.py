with open('apache_logs.txt', 'r',encoding='utf-8') as arq:
    texto = arq.read()
    # print(texto)

lista_dados = []
lista_dados.append(texto)

dic_dados = {'IP de origem': lista_dados[0], 'identd': lista_dados[1], 'user': lista_dados[2], 'data/hora': lista_dados[3], 'Requisição HTTP': lista_dados[4], 'Código de status HTTP': lista_dados[5], 'Bytes': lista_dados[6], 'Pagina de origem': lista_dados[7], 'Navegador': lista_dados[9]}
