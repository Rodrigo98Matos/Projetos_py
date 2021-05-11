lista = []
par = []
for i in range(4):
    n = int(input('Digite um número inteiro:\t'))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    if i == 0:
        c = 0
    if n == 9:
        c += 1
tupla = tuple(lista)
print(f'A)\tO valor 9 apareceu {tupla.count(9)} vezes')
print(f'B)\tO primeiro 3 foi digitado na posição:\t{tupla.index(3)+1}°') if tupla.count(3) != 0 else print('B)\tO valor 3 não foi digitado')
print(f'C)\tOs números pares são:\t{par}')
