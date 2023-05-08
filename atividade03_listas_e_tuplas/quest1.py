listas_times = ('Atlético-PE', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'Amperica-MG', 'Atléticos-GO', 'Santos', 'Ceará SC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')

primeiros_times = listas_times[0:5]
ultimno_times = listas_times[-4:]
posicap_palemiras = listas_times.index("Palmeiras")
estado_riodejaneiro = listas_times[1], listas_times[6]

print(f'Os primeiros são {sorted(primeiros_times)}')
print(f'Os últimos 4 {sorted(ultimno_times)}')
print(f'Times do estados do Rio de Janeiro {sorted(estado_riodejaneiro)}')
print(f'O Palmeiras está na {posicap_palemiras+1} posição.')