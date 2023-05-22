import pickle

nomegmail = []

while True:
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    if nome == 'END' or nome == 'end':
        break
    if email == 'END' or email =='END':
        break
    nomegmail += nome
    nomegmail += email
print(nomegmail)


# nomeegmail = {'nome':'endrew', 'email':'endrew.sousa@escolar.ifrn.edu.br',
# 'nome':'werdne', 'email':'wernde.sousa@gmail.com',
# 'nome':'endy', 'email':'endy.sousa@gmailm.com'}

# nomesemail = open('nomeegmail.pkl', 'wb')

# pickle.dump(nomeegmail, nomesemail)
# nomesemail.close()

# print(nomesemail)