from datetime import date
y = int(date.today().year)
m = 0
n = 0
for c in range(0, 7):
    a = int(input('Digite o ano de nascimento: '))
    if y - a < 18:
        m += 1
    if y - a >= 18:
        n += 1
print('{} são maiores de idade e {} são menores de idade!'.format(n, m))
