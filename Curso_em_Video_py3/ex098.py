from time import sleep
def contador(i,f,p):
    if p == 0:
        p = 1
    p = abs(p)
    if i > f:
        p = -1*(p)
        f = f-2
    for i in range(i,f+1,p):
        sleep(1)
        print(f'{i}', end = '\t', flush=True)
    print('')
def linha(n):
    print('-'*n, flush=True)


linha(84)
contador(1, 10, 1)
linha(40)
contador(10, 0, 2)
linha(50)
contador(int(input('Inicio:\t')), int(input('Fim:\t')), int(input('Passo:\t')))
