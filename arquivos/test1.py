import pickle
import csv

nomegmail = []

while True:
    nome = input('Digite seu nome: ')
    if nome == 'END' or nome == 'end':
        break
    email = input('Digite seu email: ')
    if email == 'END' or email =='END':
        break
    pessoas = [nome,email]
    nomegmail.append(pessoas)

print(nomegmail)

# modo manual:
def transforma_dado(dado):
    lista_str = []
    for pessoa in dado:
        lista_str.append(",".join(pessoa))
    return "\n".join(lista_str)

# modo csv:
with open('pessoa_csv.txt', 'wt') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(nomegmail)

# modo pickle
# with open('pessoas_pickle.txt', 'rb') as f:
#     dado = pickle.load(f)