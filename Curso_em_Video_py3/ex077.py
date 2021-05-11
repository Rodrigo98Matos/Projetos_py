Palavras = ('Rodrigo', 'Alberto', 'Matos', 'de', 'Carvalho', 'Roselia',
            'Ferreira', 'Matos', 'de', 'Carvalho')
Vogais = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
for pos, i in enumerate(Palavras):
    print(f"\nAs vogais de '{i}' São:")
    for c in Palavras[pos]:
        if c in Vogais:
            print(f'{c}', end = '\t')
