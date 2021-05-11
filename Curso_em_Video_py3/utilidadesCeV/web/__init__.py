'''import requests
def valida_url(url):
    while True:
        try:
            ur = requests.get(url).status_code
            if ur == 200:
                return True
            else:
                return False
        except:
            print(f"\033[31m{url} NÃO É UMA OPÇÃO VÁLIDA, DIGITE UMA URL VÁLIDA!\033[m")
            return False'''

import urllib
import urllib.request

def valida_url(url,show=False):
    try:
        site = urllib.request.urlopen(url)
    except urllib.error.URLError:
        print('O site não está disponivel no momento!')
        return False
    else:
        print('Consegui acessar o site com sucesso!')
        if show:
            return site.read()
        else:
            return True
