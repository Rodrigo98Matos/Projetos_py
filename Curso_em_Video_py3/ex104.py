from time import sleep
from ex102 import fatorial
def leiaint(frase):
    """
    -> Verifica se o valor inserido é um número inteiro, e retorna no número inteiro.
    :param frase: Recebe uma frase a ser exibida ao ser recebido o valor a ser verificado.
    :return: O valor numérico N inteiro.
    """
    while True:
        n = str(input(frase))
        verif = True
        if n.isnumeric():
            verif = True
        else:
            verif = False
        if verif:
            n = int(n)
            break
        else:
            print(f"\033[31m{n} NÃO É UMA OPÇÃO VÁLIDA, DIGITE APENAS UM NÚMERO INTEIRO!\033[m", flush=True)
            sleep(1)
    return n


fatorial(leiaint("Digite um número:\t"),show=True)
