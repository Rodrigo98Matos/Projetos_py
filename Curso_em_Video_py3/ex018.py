from math import radians, sin, cos, tan
'''o = float(input('Comprimento do cateto oposto: '))
a = float(input('comprimento do cateto adjacente: '))
print(' a hipotenusa é igual a: {:.2f}'.format(hypot(o, a)))'''

n = float(input('Insira um ângulo: '))
print('o seno do ângulo {}° é {:.3f}'.format(n, sin(radians(n))))
print('O cosseno de {}° é {:.3f}'.format(n, cos(radians(n))))
print('A tangente de {}° é {:.3f}'.format(n, tan(radians(n))))
