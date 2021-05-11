from random import randint
lista = []
for i in range(5):
    r = randint(0, 10)
    lista.append(r)
   
tupla = tuple(lista)
print(f'Números sorteados {tupla}, o maior número é {max(tupla)} e o menor número é {min(tupla)}')
