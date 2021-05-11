f = input('Frase: ').strip().lower().lower()
print('Quantas vezes aparece a letra a? {}'.format(f.count('a')))
print('Primeira letra a em: {}'.format(f.find('a')+1))
print('Ultima letra a em: {}'.format(f.rfind('a')+1))
