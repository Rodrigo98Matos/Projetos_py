s = input('Nome Completo: ').strip().upper()
s = str('SILVA' in s)
print('Tem Silva no nome? {}'.format(s.replace('True', 'Tem').replace('False', 'Não tem')))
