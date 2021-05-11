lista = []
while True:
    pos = len(lista)
    lista.append([])
    lista[pos].append(str(input("Nome:\t").strip().title()))
    lista[pos].append(float(input("Peso:\t")))
    if pos == 0:
        mais = menos = lista[pos][1]
    elif lista[pos][1] > mais:
        mais = lista[pos][1]
    elif lista[pos][1] < menos:
        menos = lista[pos][1]
    p = str(input("Adicionar mais pessoas?[Sim/Não]")).strip().upper()
    if p[0] == 'N':
        break
print(f"Foram adicionadas {len(lista)} pessoas!")
print("As pessoas mais pesadas são:\t", end = '')
for p in lista:
    if p[1] == mais:
        print(f"{p[0]},\t", end = '')
print("\nAs pessoas mais leves são:\t", end = '')
for p in lista:
    if p[1] == menos:
        print(f"{p[0]},\t", end = '')
