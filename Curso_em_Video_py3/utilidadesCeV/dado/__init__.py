from time import sleep

def leiadinheiro(frase):
    """
    -> Função recebe valor monetário.
    :param frase: Recebe uma frase a ser exibida no momento em que for receber o valor.
    :return: Valor monetário.
    """
    while True:
        din = str(input(frase)).strip().replace(',', '.')
        if din.isalpha() or din == '':
            print(f"\033[31m{din} NÃO É UMA OPÇÃO VÁLIDA!\033[m")
            sleep(1)
        else:
            din = float(din)
            return f"{din:.2f}"


def leiaint(frase):
    """
    -> Verifica se o valor inserido é um número inteiro, e retorna no número inteiro.
    :param frase: Recebe uma frase a ser exibida ao ser recebido o valor a ser verificado.
    :return: O valor numérico N inteiro.
    """
    while True:
        try:
            n = str(input(frase))
            n = int(n)
            return n
        except (KeyboardInterrupt):
            print("\033[31mO USUÁRIO PREFERIU NÃO DIGITAR ESTE VALOR!\033[m")
            n = 0
            return n
        except:
            print(f"\033[31m{n} NÃO É UMA OPÇÃO VÁLIDA, DIGITE APENAS UM NÚMERO INTEIRO!\033[m", flush=True)
            sleep(1)


def leiafloat(frase):
    while True:
        try:
            f = str(input(frase))
            f = float(f)
            return f
        except (KeyboardInterrupt):
            print("\033[31mO USUÁRIO PREFERIU NÃO DIGITAR ESTE VALOR!\033[m")
            f = 0
            return f
        except:
            print(f"\033[31m{f} NÃO É UMA OPÇÃO VÁLIDA. DIGITE APENAS UM NÚMERO REAL!\033[m", flush=True)
