c = float(input('Valor da Casa: '))
s = float(input('seu salário: '))
a = float(input('Parcelar em Quantos Anos? '))
por = float(s * 0.30)
vp = float(c//(a*12))
if vp < por:
    print('\033[32mEmprestimo aceito, o valor é: R${}'.format(vp))
else:
    print('\033[31mNão é possivel efetuar o eprestimo, valor da parcela superior a trinta porcento do seu salário!')
