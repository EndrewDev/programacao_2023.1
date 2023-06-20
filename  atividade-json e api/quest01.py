import httpx

lists_dados = []

# params = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5', 'key6': 'value6', 'key7': 'value7', 'key8': 'value8', 'key9': 'value9'}
url = httpx.get('https://drive.google.com/file/d/1HXpJd6bj80xBoINQhJFmiZtnqNrgf_i-/view')
lists_dados.append(url)

dic_dados = {'IP de origem': lists_dados[0], 'identd': lists_dados[1], 'user': lists_dados[2], 'data/hora': lists_dados[3], 'Requisição HTTP': lists_dados[4], 'Código de status HTTP': lists_dados[5], 'Tamanho do objeto retornado': lists_dados[7], 'Referer': lists_dados[8], 'Agente': lists_dados[9]}

print(lists_dados)

# print(url.headers)

# with httpx.stream("GET", "https://drive.google.com/file/d/1HXpJd6bj80xBoINQhJFmiZtnqNrgf_i-/view") as r:
#      for line in r.iter_lines():
#          print(line)