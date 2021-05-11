def escreva(tx,cor="\033[m"):
    print(cor,end='')
    x = len(tx) + 2
    print('-'*x)
    print(f" {tx} ")
    print('-'*x)


#escreva(str(input('Mensagem:\t')))
