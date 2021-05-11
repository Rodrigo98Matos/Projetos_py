lista = list()
while True:
    lista.append(int(input("Digite um número:\t")))
    while True:
        p = str(input("Digitar mais números?[S/N]\t").strip())[0].upper()
        if p in 'SN':
            break
        else:
            print("\033[31mDigite uma opção válida!\033[m")
    if p == 'N':
        break
lista.sort(reverse=True)
print(f"Foram digitados {len(lista)} números e são {lista}")
if 5 in lista:
    print("\033[32mO valor 5 faz parte da lista!\033[m")
else:
    print("\033[31mO valor 5 não faz parte da lista!\033[m")
