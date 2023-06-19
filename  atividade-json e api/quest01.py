import httpx

lists_dados = []
dic_dados = {}

url = httpx.post('https://drive.google.com/file/d/1HXpJd6bj80xBoINQhJFmiZtnqNrgf_i-/view' data={'kay': 'value'})
# lists_dados.append(url)

# print(lists_dados)

outrourl = url.url

print(outrourl)