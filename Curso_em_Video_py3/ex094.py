pessoas = []
s = 0
while True:
    pessoa = {
        'nome': str(input("Nome:\t").strip()).title()
    }
    while True:
        pessoa['sexo'] = str(input("Sexo[M\F]:\t").strip())[0].upper()
        if pessoa['sexo'] in 'FM':
            break
        else:
            print("\033[31mOPÇÃO INVÁLIDA!\033[m")
    pessoa['idade'] = int(input("Idade:\t"))
    s += pessoa['idade']
    pessoas.append(pessoa)
    while True:
        perg = str(input("Adicionar mais pessoas?\t").strip())[0].upper()
        if perg in 'NS':
            break
        else:
            print("\033[31mOPÇÃO INVÁLIDA!\033[m")
    if perg == 'N':
        break
fr = f"Foram cadastradas:\t{len(pessoas)}\tPessoas"
print('-'*50)
print(f'{fr: ^50}')
print('-'*50)
med = s / len(pessoas)
print(f"A média de idade do grupo de pessoas é:\t{med}")
print('-'*50)
print(f"As mulheres são:")
print('-'*50)
for m in pessoas:
    if m['sexo'] == 'F':
        print(f"{m['nome']};\t{m['idade']}")
print('-'*50)
print(f"As pessoas com idade acima da média, são:")
print('-'*50)
for m in pessoas:
    if m['idade'] > med:
        print(f"{m['nome']};\t{m['sexo']};\t{m['idade']}")
print('-'*50)
