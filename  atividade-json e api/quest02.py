import httpx, json

url = httpx.get('https://cdn.apicep.com/file/apicep/59012570.json')

with open('cep.json', 'wr') as openurl:
    json_objeto = json.load(openurl)
    print(json_objeto)