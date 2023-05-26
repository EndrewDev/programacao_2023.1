# Faça um programa que contém uma função para calcular juros compostos. A função recebe três parâmetros: montante inicial, rendimento mensal e a quantidade de meses; e deve retornar o valor do montante final. Ou seja, a função calcula qual é o valor final de uma aplicação, dado o valor inicial, o rendimento mensal da aplicação e a quantidade de meses. O programa deverá solicitar essas informações do usuário e executar a função para calcular o valor final e imprimir o resultado na tela.

juro_comp = []

def juro_composto(i, j, m):
    calc = i * pow((1 + j), m)
    calc = calc - i
    return f'{calc}'

inv_inicial = float(input('Investimento Inicial: '))
juro_porc = float(input('Taxa de juro (em %): '))
quantidade_meses = int(input("Meses: "))

print(f'{juro_composto(inv_inicial, juro_porc, quantidade_meses)}')