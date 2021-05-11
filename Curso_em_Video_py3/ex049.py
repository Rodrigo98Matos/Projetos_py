n = int(input('Digite um número inteiro: '))
for c in range(1, 11):
    print('{:3} X {:3} = {:3}'.format(n, c, n * c))
