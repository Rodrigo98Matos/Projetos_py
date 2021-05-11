p = float(input('Qual é o seu peso? '))
a = float(input('Qual é a sua altura? '))
imc = p // (a*a)
print('Seu IMC é: {:.2f}'.format(imc) )
if imc < 18.5:
    print('\033[31mAbaixo do peso!')
elif 18.5 < imc <= 25:
    print('\033[32mPeso ideal!')
elif 25 < imc <= 30:
    print('\033[33mSobrepeso!')
elif 30 < imc <= 40:
    print('\033[35mObesidade!')
elif 40 < imc:
    print('\033[31mObesidade Mórbida!')
