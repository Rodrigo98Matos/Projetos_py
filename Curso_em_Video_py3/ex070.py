a = b = 0
while True:

    flag = ''
    pro = str(input('Produto:\t')).strip()
    pre = float(input('Preço:\t\t'))
    if a == 0 or pre < me:
        me = pre
        ma = pre
        c = pro
    a += pre
    if pre > 1000:
        b += 1
    while flag != 'S' and flag != 'N':
        flag = str(input('Continuar a adicionar: [S] [N]\t')).strip().upper()[0]
    if flag == 'N':
        break
print(f'O total gasto foi R${a}\n{b} produtos custam mais de R$1000\nO produduto mais barato é {c} e custa R${me}')
