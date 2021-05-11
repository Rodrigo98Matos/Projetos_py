c = input('Cidade: ').strip().upper().split()
s = str('SANTO' in c[0])
print('Começa com o nome Santo? {}'.format(s.replace('True', 'Sim').replace('False', 'Não')))
