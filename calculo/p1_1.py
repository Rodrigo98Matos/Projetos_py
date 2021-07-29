def a1 (X):
    return (X**5)-6*(X**3)-(X**2)+3


def b1 (x):
    return (x**7)-3*(x**2)+20


def bissecao(funcao, a, b,  erro = 10**(-3),n=200):
    '''
    Método da Bisseção para determinar raiz da equação
    f(x) = 0 para x entre xmin e xmax

    Retorna uma lista com as aproximações
    '''
    
    itera = 0                       #conta as iterações da função
    fxa = funcao(a)
    fxb = funcao(b)

    media = (a + b)/2
    aprox = media
    fxmed = funcao(media)

    if fxa == 0:
        aprox = a
        return aprox

    elif fxb == 0:
        aprox = b
        return aprox

    elif (fxa > 0 and fxb > 0) or (fxa < 0 and fxb < 0):                #testa se o intervalo possui uma raiz
        print(f'Erro! f({a}) e f({b}) possuem o mesmo sinal')
        return False

    while abs(a - b) >= erro:  # a função para quando o intervalo for menor ou igual ao erro
        itera += 1
        print(f'{itera}\t{aprox}')
        if itera == n:
            print("o número de iterações foi excedido!")
            break # a função é parada ao atingir um numero n de iterações

        if (fxmed > 0 and fxa > 0) or (fxmed < 0 and fxa < 0):
            a = media

        elif (fxmed > 0 and fxb > 0) or (fxmed < 0 and fxb < 0):
            b = media

        elif fxmed == 0:
            return aprox

        media = (a + b)/2
        aprox = media
        fxmed = funcao(media)

    print(aprox)
    return aprox


bissecao(a1,-5,-2)
#bissecao(b1,-5,2)
