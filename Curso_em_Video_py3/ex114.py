from utilidadesCeV import web
# print(web.valida_url('http://pudim.com.br/',True))
try:
    a = open('texte.txt','w+')
    b = (web.valida_url('file:///C:/Users/alber/Documents/MeusProjetos/Ola_Mundo/site_exemplo/index.html',True))
    a.write(f'{b}')
finally:
    a.close()