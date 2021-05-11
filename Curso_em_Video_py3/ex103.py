def ficha(nome='<Desconhecido>', gols=0):
    """
    -> Fichamento de um jogador.
    :param nome: recebe nome do jogador.
    :param gols: recebe quantidade de gols feitos pelo jogador.
    :return: O nome do jogador e a quantidade de gols feito por ele.
    """
    return nome, gols


print(ficha())
print(ficha('Rodrigo'))
print(ficha(gols=15))
print(ficha('Rodrigo',8))
