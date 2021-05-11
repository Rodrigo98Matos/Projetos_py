lista = list()
while True:
    lista.append(int(input("Digite um número inteiro:\t")))
    while True:
        p = str(input("Digitar mais números?\t").strip())[0].upper()
        if p in 'SN':
            break
        else:
            print("\033[31mDigite uma opção válida!\033[m")
    if p == 'N':
        break
par = list()
impar = list()
for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
par.sort()
impar.sort()
if 0 in par:
    par.remove(0)
print(f"Entre os números \033[32m{lista}\033[m, os números pares são: \033[33m{par}\033[m e os números ímpares são: \033[34m{impar}\033[m!")
