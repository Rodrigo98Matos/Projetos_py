s = float(input('Salário: '))
if s <= 1250:
    s = s * 1.15
if s > 1250:
    s = s * 1.1
print('Novo salário: R${}'.format(s))
