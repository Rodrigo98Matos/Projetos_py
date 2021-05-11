listas = []
lista = []
for i in range(3):
    lista.append(str(input("Nome:\t")))
    lista.append(int(input("Valor:\t")))
    listas.append(lista[:])
    lista.clear()
print(listas)
