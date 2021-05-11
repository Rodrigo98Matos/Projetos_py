lista = list()
for i in range(5):
    lista.append(int(input(f'Digite um número inteiro para a posição {i}:\t')))
print(f"Os números digitados são: {lista}")
print(f"O maior número digitado foi: {max(lista)} nas posições:", end = '')
for (pos, i) in enumerate(lista):
    if i == max(lista):
        print(f"\t{pos}", end = '')
print(f"\nO menor número digitado foi: {min(lista)} nas posições:", end = '')
for (pos, i) in enumerate(lista):
    if i == min(lista):
        print(f"\t{pos}", end = '')
