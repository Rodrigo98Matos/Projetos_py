a = b = c = 0
while True:
    flag = ''
    i = -1
    s = ''
    while i < 0:
        i = int(input('idade:\t'))
    while s != 'M' and s != 'F':
        s = str(input('Sexo [M] [F]:\t')).strip().upper()[0]
    if i > 18:
        a += 1
    if s == 'M':
        b += 1
    elif i < 20:
        c += 1
    while flag != 'S' and flag != 'N':
        flag = str(input('Você quer cadastrar mais pessoas? [S] [N]\t')).strip().upper()[0]
    if flag == 'N':
        break
print(f'Tem {a} pessoas maior de 18 anos!\nTem {b} homens!\nTem {c} mulheres com menos de 20 anos!')
