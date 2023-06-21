with open('apache_logs.txt', 'r',encoding='utf-8') as arq:
    texto = arq.read()
    # print(texto)

lista_dados = []
lista_dados.append(texto)
for i in lista_dados:
    print(f'IP de origem:', {i[0:12]}, 'identd:', {i[13]}, 'user:', {i[15]}, 'data/hora:', {i[17:45]}, 'Requisição HTTP:', {i[46:125]}, 'Código de status HTTP:', {i[126:129]}, 'Bytes:', {i[130:136]}, 'Pagina de origem:', {i[137:202]}, 'Navegador:', {i[203:324]})
