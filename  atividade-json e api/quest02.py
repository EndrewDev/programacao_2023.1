import httpx, json

url = httpx.post('https://ws.apicep.com/cep/59015-000.json')

# for i in url:

print(url.json())

# with open('cep.txt', 'rw') as openurl:
#     json_objeto = json.load(openurl)