import pickle

nomegmail = {}

while True:
    nomeemail = input('Digite nome e email por virgula: ')
    if nomeemail == 'END' or nomeemail == 'end':
        break
    nomeemail += nomeemail
print(nomeemail)


# nomeegmail = {'nome':'endrew', 'email':'endrew.sousa@escolar.ifrn.edu.br',
# 'nome':'werdne', 'email':'wernde.sousa@gmail.com',
# 'nome':'endy', 'email':'endy.sousa@gmailm.com'}

# nomesemail = open('nomeegmail.pkl', 'wb')

# pickle.dump(nomeegmail, nomesemail)
# nomesemail.close()

# print(nomesemail)