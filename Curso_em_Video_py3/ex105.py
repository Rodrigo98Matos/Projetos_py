def notas(* notas, sit=False):
    """
    -> Função que analisa as notas inseridas.
    :param notas: Uma ou mais notas dos alunos.
    :param sit: Valor logico opcional, indica se deve ou não adicionar a situação da turma.
    :return: Um dicionário com a quantidade de notas, a maior nota, a menor nota, a media da turma, a situação (opcional)
    """
    dn = {}
    if len(notas):
        n = notas
        dn['total'] = len(n)
        dn['maior'] = max(n)
        dn['menor'] = min(n)
        dn['media'] = sum(n)/len(n)
        if sit:
            if dn['media'] >= 7:
                dn['situacao'] = "BOA"
            else:
                dn['situacao'] = "RUIM"
    return dn



t1 = notas(1,2,3,4,5,6,7,8,9,0,10,1,0,1,0,10,10,10,10)
t3 = notas(10,10,20,30,40,5,6,7,8,9,10,1,0,10,10,1,0,1,0,10,10,10,10,sit=True)

print(f"{t1}\n{t3}")
