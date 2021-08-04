def eq_n_linear(x):
    return  (x**4) - 4 * (x**3) - x + 5

def particao(a, b, N):
    """
    Dados os pontos inicial $a$ e final $b$, e o número $N$
    de subintervalos da partição regular desejada, esta função
    retorna a partição regular com tais características, sob
    a forma de uma lista
    """
    lista = [a]
    delta = (b - a)/N
    for j in range(1, N+1):
        lista += [a + j * delta]
    return lista


def posfal(funcao, dominio, tol):
    '''
    Retorna uma lista com as aproximações
    '''
    x1 = dominio[0]
    x2 = dominio[-1]
    fx1 = funcao(x1)
    fx2 = funcao(x2)

    aprox = [x1, x2]

    if fx1 == 0:
        aprox += [x1]
        return aprox

    elif fx2 == 0:
        aprox += [x2]
        return aprox

    elif (fx1 > 0 and fx2 > 0) or (fx1 < 0 and fx2 < 0):
        return 'Erro! A função não muda de sinal no intervalo especificado'

    niter = 1
    while abs(aprox[-2] - aprox[-1]) >= tol and fx1 != fx2:
        x3 = x2 - fx2 * (x1 - x2)/(fx1 - fx2)
        fx3 = funcao(x3)

        print('x1 =', x1, '\b,  x2 =', x2)
        print('|x1 - x2| =', abs(x1 - x2))
        print('x['+str(niter)+'] =', x3,
              '\b,  f(x['+str(niter)+']) =', fx3, '\n')
        niter += 1
        aprox += [x3]

        if fx3 == 0:
            return aprox

        elif (fx3 > 0 and fx1 > 0) or (fx3 < 0 and fx1 < 0):
            x1, fx1 = x3, fx3

        elif (fx3 > 0 and fx2 > 0) or (fx3 < 0 and fx2 < 0):
            x2, fx2 = x3, fx3
    return aprox

resultado = posfal(eq_n_linear, particao(-1, 2,30), 0.001)
print(resultado)