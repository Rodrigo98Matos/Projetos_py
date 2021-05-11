c = 0
s = 0
p = ''
while p != 'N':
    print('Digite [S] ou [N]:\t')
    p = str(input('Você quer inserir um númro??\t')).upper().strip()[0]
    if p == 'S':
        n = float(input('Digite um número inteiro:\t'))
        n = int(n/1)
        if c == 0:
            ma = n
            me = n
        else:
            if n > ma:
                ma = n
            if n < me:
                me = n
        c += 1
        s += n
    elif p != 'S' and p != 'N':
        print('\033[31mDigite uma opção valida!\033[m')
if c != 0:
    m = float(s//c)
    print(f'a média entre todos os números inseridos é: {m}, o maior número digitado foi: {ma} e o menor número foi: {me}')
