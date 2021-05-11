
from random import choice
lista = ['Pedra', 'Papel', 'Tesoura']
pl1 = str(input('Nome: ')).strip().title()
pl = pl1.split()
p1 = str(input('Escolha entre Pedra, Papel e Tesoura: ')).strip().title()
c = choice(lista)
co = 'Computador'
if p1 == c:
    r = '\033[33mEmpate'
elif p1 == 'Pedra' and c == 'Tesoura' or p1 == 'Tesoura' and c == 'Papel' or p1 == 'Papel' and c == 'Pedra':
    r = ('\033[32m{} ganhou'.format(pl1))
elif c == 'Pedra' and p1 == 'Tesoura' or c == 'Tesoura' and p1 == 'Papel' or c == 'Papel' and p1 == 'Pedra':
    r = ('\033[31m{} ganhou'.format(co))
print('Computador: {}\n{}: {}\n{}!!!'.format(c, pl[0], p1, r))
