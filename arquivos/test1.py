import pickle

nomegmail = []

while True:
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    if nome == 'END' or nome == 'end':
        break
    if email == 'END' or email =='END':
        break
    nomegmail.append(nome)
    nomegmail.append(email)
print(nomegmail)

nomesemail = open('nomeegmail.pkl', 'wb')
pickle.dump(nomegmail, nomesemail)
nomesemail.close()
print(nomesemail)