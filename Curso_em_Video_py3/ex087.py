matriz = [[],[],[]]
print('-'*30)
print(f"{'MATRIZ(3x3)': ^30}")
print('-'*30)
for i in range(3):
    matriz[i].append(int(input(f"({i+1},1):\t")))
    matriz[i].append(int(input(f"({i+1},2):\t")))
    matriz[i].append(int(input(f"({i+1},3):\t")))
print('-'*30)
for i in matriz:
    print(f"|\t{i[0]: ^4}\t{i[1]: ^4}\t{i[2]: ^4}\t|")
s = 0
for linha in matriz:
    for v in linha:
        if v % 2 == 0:
            s += v
print(f"a soma dos valores pares da matriz é :\t{s}")
print(f"A soma dos valores da 3ª coluna é:\t{matriz[0][2] + matriz[1][2] + matriz[2][2]}")
print(f"O maior valor da 2ª linha é:\t{max(matriz[1])}")
