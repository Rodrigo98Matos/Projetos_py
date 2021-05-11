'''def aumentar(din, por, moe=False):
    """
    -> Função aumenta o valor recebido.
    :param din: Recebe o valor a ser aumentado.
    :param por: Recebe a porcentagem a ser somada no valor din.
    :param moe: Recebe um valor lógico para indicar se o o valor sera retornado como um valor monetário, por padrão é False.
    :return: din aumentado em por%.
    """
    por /= 100
    r = din + por * din
    if moe:
        return moeda(r)
    else:
        return r
def diminuir(din, por, moe=False):
    """
    -> Função diminui o valor recebido.
    :param din: Recebe o valor a ser diminuido.
    :param por: Recebe a porcentagem a ser subitraida do valor din.
    :param moe: Recebe um valor lógico para indicar se o o valor sera retornado como um valor monetário, por padrão é False.
    :return: din diminuido em por%.
    """
    por /= 100
    r = din - por * din
    if moe:
        return moeda(r)
    else:
        return r
def dobro(din, moe=False):
    """
    -> Função dobra o valor recebido.
    :param din: Recebe o valor a ser dobrado.
    :param moe: Recebe um valor lógico para indicar se o o valor sera retornado como um valor monetário, por padrão é False.
    :return: O dobro do valor din.
    """
    r = din * 2
    if moe:
        return moeda(r)
    else:
        return r
def metade(din,moe=False):
    """
    -> Função divide pela metade o valor recebido.
    :param din: Recebe o valor a ser dividido pela metade.
    :param moe: Recebe um valor lógico para indicar se o o valor sera retornado como um valor monetário, por padrão é False.
    :return: O valor din dividido pro 2, se o parâmetro moe = True retorna o valor din formatado como um valor monetário.
    """
    r = din / 2
    if moe:
        return moeda(r)
    else:
        return r
def moeda(din):
    """
    -> Função formata o valor recebido como um valor um valor monetário.
    :param din: Recebe o valor a ser formatado.
    :return: O valor din formatado como um valor monetário.
    """
    return f"{din:.2f}"
def resumo(fun):
    """
    -> Função retorna docstrings de outras funções.
    :param fun: Recebe função a ser exibida.
    :return: docstrings da função recebida.
    """
    return help(fun)
'''
