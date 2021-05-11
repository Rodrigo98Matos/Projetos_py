h=float(input('inserir altura da parede, em metros:'))
b=float(input('inserir largora da parede, em metros:'))
t=float(input('um litro de tinta pintam quantos metros quadrados?'))
print('serão necessarios {} litros de tinta para pintar a parede de {} M²'.format((b*h)/t, b*h))
