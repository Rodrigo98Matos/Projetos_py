from utilidadesCeV.moeda import aumentar, diminuir, dobro, metade
d = float(input("Digite um valor:\t"))
pa = float(input("Inserir a porcentagem a ser aumentada:\t"))
pd = float(input("Inserir a porcentagem a ser diminuida:\t"))
print(f'''O dobro de {d} é {dobro(d)}
A metade de {d} é {metade(d)}
{d} aumentado em {pa}% é {aumentar(d, pa)}
{d} diminuido em {pd}% é {diminuir(d, pd)}''')
