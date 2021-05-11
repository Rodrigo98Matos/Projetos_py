alunos = []
#[0] = nome, [1] = p1, [2] = p2, [3] = média
print('-'*57)
print(f"|{'ADICIONAR ALUNOS': ^55}|")
print('-'*57)
while True:
    aluno = []
    aluno.append(str(input("NOME DO ALUNO:\t").strip().title()))
    aluno.append(float(input("1ª NOTA:\t")))
    aluno.append(float(input("2ª NOTA:\t")))
    aluno.append((aluno[1] + aluno[2])/2)
    alunos.append(aluno)
    p = str(input("Adicionar mais alunos?[Sim/Não]\t").strip())[0].upper()
    if p == 'N':
        break
print('-'*57)
print(f"|{'BOLETIM': ^55}|")
print('-'*57)
print(f"|{'CÓDIGO': ^6}|{'ALUNO(a)': ^40}|{'MÉDIA': ^7}|")
print('-'*57)
for pos, a in enumerate(alunos):
    po = pos + 1
    print(f"|[{po: ^4}]|{a[0][:40]: ^40}|{f'{a[3]:.2f}': ^7}|")
    print('-'*57)
while True:
    per = str(input("Deseja exibir notas de um aluno específico?\t").strip().upper())[0]
    if per == 'S':
        pos = int(input("Digite o código do aluno(a):\t").strip())
        print('-'*57)
        print(f"|{'CÓDIGO': ^6}|{'ALUNO(a)': ^33}|{'1ª NOTA': ^7}|{'2ª NOTA': ^7}|")
        print('-'*57)
        po = pos - 1
        a = alunos[po]
        print(f"|[{po: ^4}]|{a[0][:33]: ^33}|{f'{a[1]:.2f}': ^7}|{f'{a[2]:.2f}': ^7}|")
        print('-'*57)
    elif per == 'N':
        break
    else:
        print("\033[31mESCOLHA UMA OPÇÃO VÁLIDA!\033[m")
