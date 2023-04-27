import random
pessoas = []

nome = input('Digite alunos separa por virgular: ')
pessoas = nome.split(',')

print(f'listas dos alunos {pessoas}')

aleatoriamente = random.choice(pessoas)
print(f'Aluno escolhido aleatoriamente {aleatoriamente}')