import httpx

lists_dados = []

url = httpx.put('https://drive.google.com/file/d/1HXpJd6bj80xBoINQhJFmiZtnqNrgf_i-/view', data={'key': 'value'})
lists_dados.append(url)

print(lists_dados)