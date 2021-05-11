n = 0
c = 0
s = 0
print('Digite [999] para parar!')
while n != 999:
    n = int(input('Digite um número:\t'))
    if n != 999:
        c += 1
        s += n
print(f'Foram digitados {c} números e a soma destes números é {s}')
