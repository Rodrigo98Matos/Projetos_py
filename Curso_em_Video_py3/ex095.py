jogadores = []
while True:
    jogador = {'nome': str(input('Nome do jogador:\t'))}
    jogador['part'] = int(input('Quantidade de partidas jogadas:\t'))
    jogador['gols'] = []
    for i in range(jogador['part']):
        jogador['gols'].append(int(input(f"Gols feitos no {i+1} jogo:\t")))
    jogador['soma'] = 0
    for j in jogador['gols']:
        jogador['soma'] += j
    jogador['media'] = jogador['soma']/jogador['part']
    jogadores.append(jogador)
    per = str(input("Adicionar mais jogadores?[S/N]\t").strip())[0].upper()
    if per == 'N':
        break
print('-'*80)
for i, j in enumerate(jogadores):
    print(f"Código\t{i}\tNome:\t{j['nome']}\tPartidas Jogadas:\t{j['part']}\tMedia\t{j['media']}")
    print('-'*80)
while True:
    p = str(input("vizualizar jogador especifico?[S/N]\t").strip())[0].upper()
    if p == 'N':
        break
    elif p == 'S':
        e = int(input("Código do jogador:\t"))
        if e < len(jogadores):
            print('-'*50)
            print(f"Jogador\t{jogadores[e]['nome']}\tGols em partidas:")
            print('-'*50)
            for n, g in enumerate(jogadores[e]['gols']):
                print(f"Jogo\t{n+1}\t|\t{g ^4}\tgols")
        else:
            print("\033[31mOPÇÃO INVALIDA!\033[m")
    else:
        print("\033[31mOPIÇÃO INVALIDA!\033[m")
