distancia = float(input('Distância da viagem em Km: '))
if distancia <= 200:
    pre = distancia * 0.50
else:
    pre = distancia * 0.45
print('Valor da viagem: R${:.2f}'.format(pre))
