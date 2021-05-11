import matplotlib.pyplot as mp
jogador = {'nome': str(input('Nome do jogador:\t')).strip().title(), 'part': int(input('Quantidade de partidas jogadas:\t')), 'gols': [], 'soma': 0}
for i in range(jogador['part']):
    jogador['gols'].append(int(input(f"Gols feitos no jogo {i+1}:\t")))
for j in jogador['gols']:
    jogador['soma'] += j
jogador['media'] = jogador['soma']/jogador['part']
print(f"Média:\t{jogador['media']:.2f}\tTotalo de gols\t{jogador['soma']}")
print('-'*50)
print(f"Gols do jogador {jogador['nome']} em partidas:")
for i, g in enumerate(jogador['gols']):
    print(f"|{i+1}ª Partida\t|\t{g}\tgols|")
x = range(1,jogador['part']+1)
mp.plot(x, jogador['gols'])
mp.show()
