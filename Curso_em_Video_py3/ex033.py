n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))
'''if n1 <= n2 <= n3:
    print('O mairo número é: {}\nE o menor é: {}'.format(n3, n1))
else:
    if n1 <= n3 <= n2:
        print('O maior Número é: {}\nE o menor é: {}'.format(n2, n1))
    else:
        if n2 <= n1 <= n3:
            print('O maior número é: {}\nE o menor é: {}'.format(n3, n2))
        else:
            if n2 <= n3 <= n1:
                print('O maior número é: {}\nE o menor é: {}'.format(n1, n2))
            else:
                if n3 <= n1 <= n2:
                    print('O maior número é: {}\nE o menor  é: {}'.format(n2, n3))
                else:
                    if n3 <= n2 <= n1:
                        print('O maior número é: {}\nE o menor é: {}'.format(n1, n3))'''
me = n1
if n2 < n1 and n2 < n3:
    me = n2
if n3 < n1 and n3 < n2:
    me = n3
ma = n1
if n2 > n1 and n2 > n3:
    ma = n2
if n3 > n1 and n3 > n2:
    ma = n3
print('O maior valor é: {}\nE o menor é: {}'.format(ma, me))
