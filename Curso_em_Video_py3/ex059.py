from time import sleep
n1 = int(input('Digite um número:\t'))
n2 = int(input('Digite outro número\t'))
o = 1
while o != 0:
    print('-=-' * 6)
    print('''Escolha uma opção
    [1] Soma
    [2] Multiplicação
    [3] Qual é maior?
    [4] Novos números
    [0] Sair''')
    print('-=-' * 6)
    o = int(input('>>>'))
    if o == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif o == 2:
        print(f'O produto da multiplicação entre {n1} e {n2} é {n1 * n2}')
    elif o == 3:
        if n1 > n2:
            print(f'{n1} é maior!')
        elif n1 < n2:
            print(f'{n2} é maior!')
        else:
            print(f'{n1} e {n2} são iguis!')
    elif o == 4:
        n1 = int(input('Digite um número:\t'))
        n2 = int(input('Digite outro número\t'))
    else:
        print('Escolha uma opção Valida!')
    sleep(2)
print('Fim do Programa, volte sempre!')
