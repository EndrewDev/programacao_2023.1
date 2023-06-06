import os

diretorio = input('Digite um nome de diretório para que quer achar: ')
caminho1 = os.path.isdir(diretorio)
if diretorio != caminho1:
    print('Diretório não existe')
    diret = input('Digite o mesmo nome para criar diretório: ')
else:
    print('Diretório existe')

documentos = input('Digite um nome de documentos para quer entrar ')
caminho2 = os.path.isdir(documentos)
if documentos != caminho2:
    print('Diretório não existe')
    docum = input('Digite segundo nome de diretório: ')
else:
    print('Diretório existe')

text = input('Digite um nome de pasta para ler: ')
caminho3 = os.path.isfile(text)
if text != caminho3:
    print('Essa pasta não existe')
    texto = input('Digite um nome da pasta: ')
else:
    print('Diretório existe')


caminho4 = print(f'/{diretorio}/{documentos}/{text}')
existe = os.path.exists(caminho4)

if caminho4 != existe:
    print('Achamos')
else:
    print('Isso não existe')


caminho5 = os.makedirs(diret, docum)

caminho_origi = os.path.exists(caminho5)
if caminho5 != caminho_origi:
    print('Isso não existe')
else:
    print('Existe')