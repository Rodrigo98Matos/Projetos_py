from datetime import date
a = int(input('Ano de nascimento do nadador: '))
y = int(date.today().year)
i = y - a
if i <= 9:
    print('\033[31mO nadador está na categoria Mirim!')
elif i <= 14:
    print('\033[32mO nadador está na categoria Infantil!')
elif i <= 19:
    print('\033[33mO nadador está na categoria Junior!')
elif i <= 25:
    print('\033[34mO nadador está na categoria Sênhor!')
else:
    print('\033[35mO nadador está na categoria Master!')
