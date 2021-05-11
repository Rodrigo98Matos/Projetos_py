from random import randint
cont = 0
while True:
    print('-=-'*10)
    p = str(input('Par[P] ou Impar[I]?\t')).strip().upper()[0]
    c = randint(0, 5)
    n = int(input('Escolha um número [0 - 5]'))
    print(f'Computador:\t{c}\nJogador:\t{n}')
    if p == 'p' and (c + n) % 2 == 0 or p == 'I' and (c + n) % 2 != 0:
        print('\033[32mParabéns!\033[33m✨\033[m')
        cont += 1
    else:
        print('\033[31mVocê perdeu!\033[m')
        break
print(f'Você conseguiu vencer apenas {cont} vez') if cont == 1 else print(f'Você conseguiu vencer {cont} vezes seguidas')
