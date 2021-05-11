s = str(input('Sexo [M/F]: ')).strip().upper()
while s != 'F' and s != 'M':
    print('Dado invalido!')
    s = str(input('Sexo [M/F]: ')).strip().upper()
    print(s)
if s == 'M':
    sexo = 'Masculino'
elif s == 'F':
    sexo = 'Feminino'
print(f'Sexo {sexo} registrado com sucesso!')
