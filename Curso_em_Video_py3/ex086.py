matriz = [[],[],[]]
print('-'*30)
print(f"{'MATRIZ(3x3)': ^30}")
print('-'*30)
for i in range(3):
    matriz[i] = [(int(input(f"({i+1},1):\t"))), (int(input(f"({i+1},2):\t"))), (int(input(f"({i+1},3):\t")))]
print('-'*30)
for i in matriz:
    print(f"|\t{i[0]: ^4}\t{i[1]: ^4}\t{i[2]: ^4}\t|")
