from time import sleep
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
           'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', ' Treze',
           'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')

while True:
    while True:
        n = int(input('Digite um número inteiro [0 - 20]:\t'))
        if 0 <= n <= 20:
            break
        print('Apenas números do entervalo [0 - 20]!')
        sleep(0.5)
    for pos, c in enumerate(extenso):
        if n == pos:
            print(f'{n} Por extenso é {extenso[pos]}')
            sleep(2)
    while True:
        p = str(input('Quer incluir mais números?[S/N]\t')).strip().upper()[0]
        if p == 'S' or p == 'N':
            break
        print('Responda apenas, Sim ou Não!')
        
        sleep(1.5)
    if p == 'N':
        break
