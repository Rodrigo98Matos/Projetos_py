from termcolor import colored

v = float(input('Velocidade do carro, em Km/h: '))
if v > 80:
    print(colored('Ultrapassou a velocidade de 80Km/h, multa de: R${}'.format(7 * (v - 80)), 'red'))
else:
    print(colored('Tenha um bom dia, dirija com seguraça!', 'green'))
