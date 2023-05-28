# Faça um programa que contém uma função para calcular juros compostos. A função recebe três parâmetros: montante inicial, rendimento mensal e a quantidade de meses; e deve retornar o valor do montante final. Ou seja, a função calcula qual é o valor final de uma aplicação, dado o valor inicial, o rendimento mensal da aplicação e a quantidade de meses. O programa deverá solicitar essas informações do usuário e executar a função para calcular o valor final e imprimir o resultado na tela.

import pickle

def juro_composto(i, j, m):
    mont_in = []
    rend_m = []
    quant_m = []
    for m in i:
        mont_in.append(m)
    for r in j:
        rend_m.append(r)
    for q in m:
        quant_m.append(q)
    calc = mont_in * rend_m * quant_m
    print(f"Monatante inicial: {mont_in}")
    print(f"Rendimento Mensal: {rend_m}")
    print(f"Quantidade de meses: {quant_m}")
    return calc
    

capital_inicial = float(input('Investimento Inicial: '))
juro_meses = float(input('Taxa de juro (em %): '))
durante_mes = int(input("Meses: "))

print(f'{juro_composto(capital_inicial, juro_meses, durante_mes)}')

# with open()