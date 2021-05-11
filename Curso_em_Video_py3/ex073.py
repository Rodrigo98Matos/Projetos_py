Times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense',
         'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará',
         'Corinthians', 'Atlético-GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco',
         'Goiás', 'Coritiba', 'Botafogo')
print(f'Os 5 melhores colocados são:')
for t in Times[:5]:
    print(f'\t{t}')
print(f'Zona de rebaixamento: {Times[-4:]}')
for r in Times[-4:]:
    print(f'\t{r}')
print(f'Em ordem alfabetica:')
for a in sorted(Times):
    print(f'\t{a}')
print(f'A Chapecoense está na posição: {Times.index(Chapecoense)+1}°!') if 'Chapecoense' in Times else print('O Time Chapecoense não está entre os 20 melhores colocados!')
