#from math import factorial
from matplotlib import pyplot

n = int(input('Digite um número:\t'))
f = 1
c = 0
'''x = []
y = []'''
for i in range(n):
    c += 1
    f *= c
    '''x.append(c)
    y.append(f)'''
print(f'O fatorial de {n} é {f}')
'''pyplot.plot(x, y)
pyplot.show()
n = int(input('Digite um número'))
f = factorial(n)
print(f'O fatorial de {n} é {f}!')'''