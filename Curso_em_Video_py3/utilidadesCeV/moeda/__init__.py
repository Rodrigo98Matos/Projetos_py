def aumentar(din, por, moe=False,s='R$'):
    """
    -> Função aumenta o valor recebido.
    :param din: Recebe o valor a ser aumentado.
    :param por: Recebe a porcentagem a ser somada no valor din.
    :param moe: Recebe um valor lógico para indicar se o o valor sera retornado como um valor monetário, por padrão é False.
    :return: din aumentado em por%.
    """
    por /= 100
    r = din + por * din
    return moeda(r,s) if moe else r
def diminuir(din, por, moe=False,s='R$'):
    """
    -> Função diminui o valor recebido.
    :param din: Recebe o valor a ser diminuido.
    :param por: Recebe a porcentagem a ser subitraida do valor din.
    :param moe: Recebe um valor lógico para indicar se o o valor sera retornado como um valor monetário, por padrão é False.
    :return: din diminuido em por%.
    """
    por /= 100
    r = din - por * din
    return moeda(r,s) if moe else r
def dobro(din, moe=False,s='R$'):
    """
    -> Função dobra o valor recebido.
    :param din: Recebe o valor a ser dobrado.
    :param moe: Recebe um valor lógico para indicar se o o valor sera retornado como um valor monetário, por padrão é False.
    :return: O dobro do valor din.
    """
    r = din * 2
    return moeda(r,s) if moe else r
def metade(din,moe=False,s='R$'):
    """
    -> Função divide pela metade o valor recebido.
    :param din: Recebe o valor a ser dividido pela metade.
    :param moe: Recebe um valor lógico para indicar se o o valor sera retornado como um valor monetário, por padrão é False.
    :return: O valor din dividido pro 2, se o parâmetro moe = True retorna o valor din formatado como um valor monetário.
    """
    r = din / 2
    return moeda(r,s) if moe else r
def moeda(din,s='R$'):
    """
    -> Função formata o valor recebido como um valor um valor monetário.
    :param din: Recebe o valor a ser formatado.
    :return: O valor din formatado como um valor monetário.
    """
    return f"{s}{din:.2f}".replace('.',',')
def resumo(din,au=0,dm=0):
    """
    -> Função mostra tabela com .
    :param dim: Recebe valor a ser alterado.
    :param au: Recebe porcentagem a aumentar o valor.
    :param dm: Recebe porcentagem a reduzir o valor.
    :return: Tabela com as funções.
    """
    print('-'*50)
    print(f"{'RESUMO DO VALOR': ^50}")
    print('-'*50)
    print(f"Preço inicial: {moeda(din): >35}")
    print(f"Dobro do preço: {dobro(din, True): >34}")
    print(f"Metade do preço: {metade(din,True): >33}")
    print(f"{au: <3}% de aumento: {aumentar(din, au, True): >33}")
    print(f"{dm: <3}% de redução: {diminuir(din, dm,True): >33}")
    print('-'*50)
