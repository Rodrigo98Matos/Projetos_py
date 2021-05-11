from random import randint
from time import sleep
j = 11
c = randint(0, 10)
v = 0
while not j == c:
    print('-=-' * 12)
    print('Vou pensar em um número entre 0 e 10')
    print('-=-' * 12)
    j = int(input('Em que número eu pensei?\t'))
    v += 1
    print('PROCESSANDO...')
    sleep(1.5)
    if j != c:
        if j < c:
            print('Mais, Tente novamente!')
        elif j  > c:
            print('Menos, Tente novamente!')

print(f'Parabéns, você me venceu!\n O número que eu pensei foi {c}\n Você tentou {v} vezes!')
