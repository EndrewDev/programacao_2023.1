# Faça um programa que contém uma função para calcular juros compostos. A função recebe três parâmetros: montante inicial, rendimento mensal e a quantidade de meses; e deve retornar o valor do montante final. Ou seja, a função calcula qual é o valor final de uma aplicação, dado o valor inicial, o rendimento mensal da aplicação e a quantidade de meses. O programa deverá solicitar essas informações do usuário e executar a função para calcular o valor final e imprimir o resultado na tela.

import pickle

def composto(tjuro, investimento, meses):
   tjuro1=tjuros/100
   mont_final = investimento*pow(1+tjuro1,3)
   jurototal = investimento*(pow(1+tjuro1,3)-1)
   return mont_final, jurototal

mont_ini = []
rend_m = []
quant_m = []

investimento = float((input('Investimento Inicial: ')))
tjuros = float((input('Taxa de Juros (em %): ')))
meses = int(input('Meses: '))

mont_ini.append(investimento)
rend_m.append(tjuros)
quant_m.append(meses)

respo = composto(investimento, tjuros, meses)

resposta = []
for i in respo:
    resposta.append(i)

print(f'O valor futuro é de {resposta[0]}')
print(f'Os juros totais é de {resposta[1]}')

# with open()