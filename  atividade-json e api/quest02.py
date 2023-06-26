import httpx, json

url = httpx.get('https://ws.apicep.com/cep/59015-000.json')
url = url.json()

print(url)
# for i,v in url.items():
#     print('{}:{}'.format(i,v))