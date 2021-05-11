lista = list()
for count in range(5):
    while True:
        num = str(input('Digite um número:\t')).strip()
        v = 0
        for n in num:
            if n not in '0123456789':
                v += 1
        if v == 0:
            num = int(num)
            break
        else:
            print("\033[31mDigite apenas um número inteiro!\033[m")
    if count == 0:
        lista.append(num)
        print(f"\033[32m{num} foi adicionado no começo da lista!\033[m")
    elif num <= min(lista):
        lista.insert(0,num)
        print(f"\033[32m{num} foi adicionado no começo da lista!\033[m")
    elif num >= max(lista):
        lista.append(num)
        print(f"\033[32m{num} foi adicionado no final da lista!\033[m")
    else:
        ants = lista[0]
        for atual in lista:
            atual
            if ants < num <= atual:
                lista.insert(lista.index(atual),num)
                break
            ants = atual
        print(f"\033[32m{num} foi adicionado na posição {lista.index(num)}!\033[m")
print(lista)
