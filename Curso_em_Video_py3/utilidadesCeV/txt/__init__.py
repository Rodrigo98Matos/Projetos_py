from time import sleep


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




def linha(tan=83,l='-'):
    print(l*tan, flush=True)


def cabeçalho(frase, tan=83,l='-',cor='\033[m',__l='',__cor='\033[m',__linha_final=True,__linha__inicial__=True):
    if __l == '':
        __l = l
    if __linha__inicial__:
        linha(tan,l=l)
    print(cor,end='')
    print(frase.center(tan),flush=True)
    print(__cor,end='')
    if __linha_final:
        linha(tan,l=__l)


def menu(lista,tan=83):
    cabeçalho('MENU PRINCIPAL')
    tan3 = tan2 = int((tan - 7)//2)
    if tan3 % 2 != 0:
        tan3 += 1
    for i, o in enumerate(lista):
        print(f"|{f'[{i}]'.center(tan3)}  |  {o.center(tan2)}|",flush=True)
    linha(tan)
    p = leiaint(">>>")
    return p


def arquivoexiste(arq='arquivo.txt'):
    try:
        a = open(arq,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome='arquivo.txt'):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('',end='')


def cadastrar(nome='arquivo.txt'):
    try:
        arq = open(nome, 'a+')
    except:
        print('erro ao abrir o arquivo')
    else:
        test = arq.readlines()
        s = []
        s.append(str(input("Nome:\t")).strip().title())
        if s[0] == '':
            s[0] = '<desconhecido>'
        s.append(leiaint("Idade:\t"))
        try:
            arq.writelines(f'\n{s[0]};{s[1]}')
        except:
            print("\033[31mNÃO FOI POSSÍVEL CADASTRAR!\033[m")
        else:
            fr = f"\033[32m{s[0].split()[0]} CADASTRADO COM SUCESSO!\033[m"
            cabeçalho(fr)
    
    finally:
        arq.close()
        print('\033[m', end='')
        sleep(1)


def listar(cabç='Listagem'):
    cabeçalho(cabç)
    print(f"|{'Nome': ^50}|{'Idade': ^30}|")
    print('-'*83)
    try:
        arq = open('arquivo.txt', 'r')
        texto = arq.readlines()
        for l in texto :
            try:
                l = l.replace('\n','').split(';')

                print(f"{(l[0]): ^51}|{l[1]: ^3} anos de idade.")
            except:
                print('',end='')
        print('-'*83)
    finally:
        arq.close()
        sleep(1)
