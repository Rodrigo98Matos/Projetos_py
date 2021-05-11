from datetime import date
year = date.today().year
dados = {'nome': str(input('Nome:\t')).strip().title(),
        'ano': int(input('Ano de nascimento:\t')),
        'ctps': int(input('NIS:\t'))}
dados['idade'] = year - dados['ano']
if dados['ctps'] != 0:
    dados['cont'] = int(input('Ano de contratação:\t'))
    dados['sal'] = float(input('Salário:\t'))
    dados['Vai se aposentar com'] = (dados['cont'] - dados['ano']) + 35
print('-'*30)
for k, v in dados.items():
        print(f"{k}:\t{v}")
