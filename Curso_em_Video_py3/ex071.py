s = int(input('Valor a ser sacado: R$'))
c = s // 50
v = (s % 50) // 20
d = ((s % 50) % 20) // 10
u = ((s % 50) % 20) % 10
if c != 0:
    print(f'|\t[{c}]\tCédulas de\tR$50\t|')
if v != 0:
    print(f'|\t[{v}]\tCédulas de\tR$20\t|')
if d != 0:
    print(f'|\t[{d}]\tCédulas de\tR$10\t|')
if u != 0:
    print(f'|\t[{u}]\tCédulas de\tR$1\t\t|')
