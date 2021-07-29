def iteracao(a,b,erro):
    from math import log10
    return round((log10(b-a)-(log10(erro)))/log10(2))
    


def bissecao_melhor(funcao, a, b,  erro = 10**(-3)):
    '''
    Método da Bisseção para determinar raiz da equação
    f(x) = 0 para x entre a e b
    '''
    
    itera = iteracao(a,b,erro)         #conta as iterações da função
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

    for i in range(itera):
        print(f'{i+1}\t{aprox}')
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

def a1 (X):
    return (X**5)-6*(X**3)-(X**2)+3


def b1 (x):
    return (x**7)-3*(x**2)+20


bissecao_melhor(a1,-5,-2)
#bissecao_melhor(b1,-5,2)
