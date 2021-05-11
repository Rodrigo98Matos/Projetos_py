from ex097 import escreva
def manual(funcao):
    """
    ->Exibe manual da função inserida.
    :param funcao: recebe a função a ser exibido seu manual.
    :return: O help da função.
    """
    print(c[3],end='',flush=True)
    return help(funcao)


c = ("\033[m",              #0 - sem cores
     "\033[0;30;41m",       #1 - vermelho
     "\033[0;30;42m",       #2 - verde
     "\033[0;30;43m",       #3 - amarelo
     "\033[0;30;44m",       #4 - azul
     "\033[0;30;45m",       #5 - roxo
     "\033[7;30m"           #6 - branco
     )
while True:
    escreva("Exibir manual de funções",c[2])
    f = str(input(f"{c[1]}Função:[fim]enserra\t"))
    if f.upper() == 'FIM':        
        break
    manual(f)
escreva("Até logo!",c[1])
print('\033[m')
