s = 0
g = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        g += 1
print('A soma de todos os {} valores solicitados é de {}'.format(g, s))
