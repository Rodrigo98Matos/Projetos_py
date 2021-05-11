from random import randint
from time import sleep
c = randint(0, 5)
print('-=-' * 12)
print('Vou pensar em um número entre 0 e 5')
print('-=-' * 12)
j = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if j == c:
    print('Parabéns, você me venceu!')
else:
    print('Eu te venci, você disse {} mas a resposta certa é {}!'.format(j, c))
