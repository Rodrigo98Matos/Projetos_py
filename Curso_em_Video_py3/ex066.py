c = s = 0
while True:
    print('-=-' * 15)
    print('Digite Um número inteiro:\t', end = '')
    n = int(input('>>>'))
    if n != 999:
        c += 1
        s += n
    elif n == 999:
        break
print(f'Foram digitados {c} e a soma de todos é {s}')
