num = [[],[]]
for c in range(7):
    n = int(input(f"Digite o {c+1}º número:\t"))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f"Os números pares são:\t\033[33m{num[0]}\033[m\te os ímpares são:\t\033[34m{num[1]}\033[m")
