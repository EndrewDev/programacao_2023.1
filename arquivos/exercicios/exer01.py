# Faça um programa que contém uma função para calcular juros compostos. A função recebe três parâmetros: montante inicial, rendimento mensal e a quantidade de meses; e deve retornar o valor do montante final. Ou seja, a função calcula qual é o valor final de uma aplicação, dado o valor inicial, o rendimento mensal da aplicação e a quantidade de meses. O programa deverá solicitar essas informações do usuário e executar a função para calcular o valor final e imprimir o resultado na tela.

import pickle

def composto(juro, inv, mese):
    listas_composto = []
    montate = 0
    rendimento = 0
    quantidade = 0
    taxajuro = juro / 100
    mont_final = inv*pow(1+taxajuro,3)
    if montate <= inv:
        montate += inv
    elif rendimento <= juro:
        rendimento += juro
    elif quantidade <= mese:
        quantidade += mese
    listas_composto = [{'montate inicial': montate, 'rendimento mesal': rendimento, 'quantidade meses': quantidade}]
    resposta = listas_composto
    return resposta

investimento = float((input('Investimento Inicial: ')))
tjuros = float((input('Taxa de Juros (em %): ')))
meses = int(input('Meses: '))

respo = composto(tjuros, investimento, meses)
print(f'O valor montante final: {respo}')

with open('listas_composto.pck.txt', 'wb') as f:
    pickle.dump(respo, f)