aluno = {'nome': str(input('Nome do aluno:\t').strip()).title(), 'media': float(input('Média do aluno:\t'))}
if aluno['media'] >= 7:
    aluno['resultado'] = "\033[32m  APROVADO  \033[m"
elif 5 <= aluno['media'] < 7:
    aluno['resultado'] = "\033[33mRECUPERAÇÃO \033[m"
else:
    aluno['resultado'] = "\033[31m REPROVADO  \033[m"
print('-'*75)
print(f"|{'ALUNO': ^50}|{'MÉDIA': ^10}|{'SITUAÇÃO': ^12}|")
print('-'*75)
print(f"|{aluno['nome']: ^50}|{aluno['media']: ^10}|{aluno['resultado']: ^12}|")
print('-'*75)
