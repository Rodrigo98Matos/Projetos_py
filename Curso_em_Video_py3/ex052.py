n = int(input('Digite um número: '))
a = 0
for c in range(1, n+1):
    if n % c == 0:
        a += 1
        print(c)
if a == 2:
    print('{} é um número primo'.format(n))
else:
    print('{} não é um número primo'.format(n))
