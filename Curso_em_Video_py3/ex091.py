from time import sleep
from random import randint as dado
from operator import itemgetter
ranking = []
jogadores = {'Jogador 1': dado(1,6), 'Jogador 2': dado(1,6), 'Jogador 3': dado(1,6),  'Jogador 4': dado(1,6)}
for k,v in jogadores.items():
    print(f"O {k} sorteou o valor {v}")
    sleep(1)
print('-'*42)
print(f"{'RANKING': ^42}")
print('-'*42)
ranking = sorted(jogadores.items(),key=itemgetter(1),reverse=True)
for i, j in enumerate(ranking):
    print(f"{i+1}º Lugar:\t{j[0]}\tCom\t{j[1]}")
    sleep(1)
