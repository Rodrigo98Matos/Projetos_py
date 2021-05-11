g = str(input('Digite uma frase: '))
f = g.strip().lower().split()
f = ''.join(f)
n = len(f)
s = 0
for c in range(0, n):
    if f[c] == f[-(c + 1)]:
        s = s + 1
if s == n:
    print(g, 'É um palíndromo!!!')
else:
    print(g, 'Não é um palíndromo')