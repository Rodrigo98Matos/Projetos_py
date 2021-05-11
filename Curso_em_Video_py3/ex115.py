from utilidadesCeV.txt import *
from utilidadesCeV.dado import leiaint
if not arquivoexiste():
    criararquivo()
cabeçalho("SISTEMA DE ARQUIVAMENTO v1.0",cor='\033[32m')
while True:
    p = menu('ENCERRAR CADASTRAR LISTAR'.split())
    if p == 0:
        break
    elif p == 1:
        cabeçalho('NOVO CADASTRO')
        cadastrar()
    elif p == 2:
        try:
            listar()
        except:
            print('',end='')
    else:
        fra = f'\033[31mESCOLHA UMA OPÇÃO VÁLIDA!\033[m'
        print(f"{fra: ^91}")
cabeçalho('VOLTE SEMPRE!',cor='\033[34m')
