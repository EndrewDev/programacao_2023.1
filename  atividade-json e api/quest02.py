import httpx

url = httpx.get('https://cdn.apicep.com/file/apicep/59012570.json')

print(url)