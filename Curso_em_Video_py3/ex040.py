n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
m = (n1 + n2 + n3)//3
print('Sua média é: {:.2f}'.format(m))
if m >= 7:
    print('\033[32mAprovado!!!\033[m')
elif m < 7:
    if 4 <= m <7:
        print('\033[33mPrecisa fazer a reposição!')
    elif m < 4:
        print('\033[31mReprovado!')
        print('Um período jogado fora!!!')
