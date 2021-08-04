def funcao_4 (X):
    return (X**3)-(X**2)+3

def particao(a, b, N):
    lista = [a]
    delta = (b - a)/N
    for j in range(1, N+1):
        lista += [a + j * delta]
    return lista

def pontofixo(funcao, dominio, k, MAX):
    '''
    Método do Ponto Fixo
    Retorna uma lista com as aproximações
    '''
    tol = 10**(-3)
    medio = (dominio[0] + dominio[-1])/2.0
    if abs(funcao(medio)) < tol:
        return [medio]
    def g(x):
        return x - k*funcao(x)
    if g(medio) < dominio[0] or g(medio) > dominio[-1]:
        print('Erro! Não há ponto fixo.')
        aprox = False
    elif g(medio) >= dominio[0] and g(medio) <= dominio[-1]:
        aprox = [medio, g(medio)]
        num = 3  # numero de iteracoes
        while abs(funcao(aprox[-1])) >= tol and num <= MAX:
            aprox += [g(aprox[-1])]
            num += 1
    else:
        print('Erro!')
        aprox = False
    return aprox

print(pontofixo(funcao_4,particao(0,1,50),0.1, 50))
