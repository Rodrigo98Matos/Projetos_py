print('-=-'*11)
print('Gerador de Sequência de Fibonacci')
print('-=-'*11)
n = int(input('Quantidade de termos:\t'))
t1 = 0
t2 = 1
for i in range(n):
    print(t2)
    t3 = t1 + t2
    t1 = t2
    t2 = t3
