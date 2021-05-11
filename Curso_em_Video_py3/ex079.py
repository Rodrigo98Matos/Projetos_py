lista = list()
while True:
    while True:
        num = str(input('Digite um número inteiro:\t'))
        v = 0
        for n in num:
            if n not in '0123456789':
                v += 1
        if v == 0:
            num = int(num)
            break
        else:
            print('\033[31mDigite apenas números!\033[m')
    if num not in lista:
        lista.append(num)
    else:
        print(f"\033[31mO número {num} já foi digitado\033[m")
    while True:
        p = str(input('Digitar mais números?[Sim ou Não]\t').strip())[0].upper()
        if p in 'NS':
            break
    if p == 'N':
        break
print(f"O números digitados corretamente são:", end ='')
lista.sort()
for i in lista:
    print(f"\t{i}", end = '')
