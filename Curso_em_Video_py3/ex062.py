i = int(input('Digite o inicio da PA:\t'))
r = int(input('Digite a razão da PA:\t'))
c = 0
m = 1
s = 10
while c < s:

    print(f'{i}')
    i += r
    c += 1
while m != 0:
    m = int(input('Quantos termos a mais você quer?\t'))
    s += m
    c = 1
    while c <= m:
        print(f'{i}')
        i += r
        c += 1
print(f'A PA foi finalizada com {s} termos mostrados')
