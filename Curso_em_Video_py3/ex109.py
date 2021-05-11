from utilidadesCeV.moeda import diminuir, dobro, aumentar, metade
d = 1000
print(d)
print(f"Diminui:    {diminuir(d, 33.3333333)}   ->  {diminuir(d, 33.3333333,moe=True)}")
print(f"Aumenta:    {aumentar(d, 20)}   ->  {aumentar(d, 20,moe=True)}")
print(f"Dobro:      {dobro(d)}  ->  {dobro(d,moe=True)}")
print(f"Metade:     {metade(d)} ->  {metade(d,moe=True)}")
