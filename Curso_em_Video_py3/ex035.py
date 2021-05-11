r1 = float(input('comprimento da reta 1: '))
r2 = float(input('Comprimento da reta 2: '))
r3 = float(input('Comprimento da reta 3: '))
if r1 < (r2+r3) and r2 < (r1+r3) and r3 < (r1+r2):
    print('Sim, é possível formar um triângulo!')
else:
    print('Não, não é possível formar um triângulo!')
