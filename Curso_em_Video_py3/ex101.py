def voto(a):
    """
    ->Verificador de Cidadão votante.
    :param a: recebe o ano de nascimento do usuário e verifica se o voto do usuário é Obrigatório, Opcional ou Negado.
    :return: Um valor literal, uma frase.
    """
    from datetime import date
    y = date.today().year
    idade = y - a
    if idade >= 65 or 16 <= idade <18:
        r = f"Com {idade} anos, o voto é \033[33mOPCIONAL\033[m"
    elif 18 <= idade < 60:
        r = f"Com {idade} anos, o voto é \033[32mOBRIGATÓRIO\033[m"
    else:
        r = f"Com {idade} anos, o voto é \033[31mNEGADO\033[m"
    return r


print(voto(int(input("Ano de nascimento:\t"))))
