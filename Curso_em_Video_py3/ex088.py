from time import sleep
from random import sample
palpites = []
mega = range(1, 61)
print('-'*30)
print(f"{'MEGA-SENA': ^30}")
print('-'*30)
n = int(input("Quantidade de jogos a serem gerados:\t"))
for c in range(n):
    palpites.append(sample(mega, 6))
print('-'*30)
for i, j in enumerate(palpites):
    j.sort()
    print(f"Jogo {i}:\t{j}")
    sleep(1)
print('-'*30)
