produtos = ('Arroz', 8.90, 'Feijão', 6.5, 'lapiz', 1, 'Leite', 5.50, 'Flocos', 1.70)
print('-'*30)
s = 'Preço dos Produtos'
print(f'{s: ^30}')
for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:-<24}R${produtos[i+1]:>6.2f}')
print('-'*30)
