from random import sample
def sorteia(n):
    return sample(range(n+1),5)
def somapar(l):
    s = 0
    for i in l:
        if i % 2 == 0:
            s += i
    return s
num = sorteia(100)
print(f"Os números sorteados:\t{num}")
print(f"Soma dos números pares sorteados:\t{somapar(num)}")
