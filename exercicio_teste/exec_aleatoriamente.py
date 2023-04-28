# import random
# pessoas = []

# nome = input('Digite alunos separa por virgular: ')
# pessoas = nome.split(',')

# print(f'listas dos alunos {pessoas}')

# aleatoriamente = random.choice(pessoas)
# print(f'Aluno escolhido aleatoriamente {aleatoriamente}')

# or like this

import random

aluno = []

for i in range(4):
    alunos2 = input('Digite os nomes quatros alunos:\n')

aluno.append(alunos2)
# aleatoriamente = random.choice[aluno]

print(f'Aluno(a) escolhindo aleatoriamente: {random.choice[aluno]}')