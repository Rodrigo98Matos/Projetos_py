p = float(input('Preço inicial do produto: '))
print('''Digite
[1] A vista com dinheiro
[2] Débito no cartão
[3] Parcelamento no cartão, até 2x sem juros! ''')
f = int(input('Qual é a forma de pagamento, dinheiro ou parcelamento no cartão: '))
if f == 1:
    v = p * 0.9
    print('O valor a ser pago será: R${}'.format(v))
elif f == 2:
    v = p * 0.95
    print('O valor a ser pago será: R${}'.format(v))
elif f == 3:
    m = int(input('Quantedade de parcelas: '))
    if m <= 2:
        v = p // m
        print('O valor a ser pago será: R${}'.format(v))
    elif m > 2:
        v = (p * 1.2) // m
        print('O valor da parcela será: R${}. E o valor total a ser pago será de: R$:{}'.format(v, p*1.2))
else:
    print('Opção de pagamento Invalida')