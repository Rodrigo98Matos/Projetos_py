from datetime import date
i = int(input('Em que ano você nasceu? '))
a = int(date.today().year)
id = int(a-i)
if id < 18:
    f = 18 - id
    if id == 17:
        print(' Você deve se alistar ano que vem!')
    else:
        print('Você deve se alistar em {} anos!'.format(f))
elif id == 18:
    print('Você deve se alistar este ano!')
elif id > 18:
    print('\033[34m-=-'*20, '\033[m')
    print('Digite 1 para Homem ou 2 para Mulher')
    print('\033[34m-=-'*20, '\033[m')
    g = int(input('Você é Homem ou Mulher? '))
    if g == 2:
        print('Você não precisa se alistar!')
    else:
        print('Digite 3 para sim ou 4 para não!')
        b = int(input('Você já se alistou nas forças armadas? '))
        if b == 3:
            print('OK, Voce já se alistou nas forças armadas!!!')
        else:
            print('Você deveria ter se alistado há {} anos!'.format(id-18))
