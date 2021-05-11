v1 = int(input('\033[32mPrimeiro número: '))
v2 = int(input('Segundo número: \033[m'))
cores = {'amarelo':'\033[33m',
         'ciano':'\033[36m',
         'limpa':'\033[m'}
if v1 > v2:
    M = v1
    m = v2
if v2 > v1:
    M = v2
    m = v1
print('O número {}{}{} é maior que o número {}{}{}!'.format(cores['ciano'], M, cores['limpa'], cores['amarelo'], m, cores['limpa'])) if v1 != v2 else print('\033[34mOs dois valores são iguais!')
