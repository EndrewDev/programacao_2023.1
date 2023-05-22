nomesegmail = []

while True:
    nome = input('Digite seu nome:\n')
    email = input('Digite seu email:\n')
    if nome == 'END' or nome == 'end':
        break
    nome += nomesegmail
    if email == 'END' or email == 'end':
        break
    email += nomesegmail

