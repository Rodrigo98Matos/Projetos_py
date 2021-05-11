from time import sleep
def fatorial(n=0,show=False):
    """
    -> Função que calcula fatorial do número inserido.
    :param n: recebe número a ser fatorado.
    :param show: recebe valor lógico True ou False para mostrar o processo de cálculo fatorial.
    :return: O valor do fatorial de um número n.
    """
    if n == 0:
        f = 0
        print(0, end = '', flush=True)
    else:
        f = 1
    for i in range(1, n+1):
        f *= i
        if i == 1:
            if show:
                print(i, end = '', flush=True)
                sleep(0.3)
        else:
            if show:
                print(f" x {i}", end = '', flush=True)
                sleep(0.3)
    if show:
        print(f" = {f}")

    return f


#print(fatorial(int(input("Inserir número:\t"))))
#fatorial(int(input("Inserir número:\t")), show=True)
