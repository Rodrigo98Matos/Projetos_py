m= 0
ih = 0
mi = 0
for c in range(0, 4):
    n = str(input('Digite nome: ')).strip().capitalize()
    i = int(input('Digite idade: '))
    s = str(input('Sexo? [M/F] ')).strip().lower()
    mi += i
    if s == 'm':
        if i > ih:
            ih = i
            h = n
    if s == 'f':
        if i < 21:
            m += 1
med = float(mi / 4)
print('A média das idades é {}, o Homem mais velho é {} e tem {} Mulhers com menos de 21 anos no grupo!'.format(med, h, m))
