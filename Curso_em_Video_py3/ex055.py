for c in range(0, 5):
    p = float(input('Digite o peso: '))
    if c == 0:
        m = p
        n = p
    else:
        if p > m:
            m = p
        if p < n:
            n = p
print('O maior peso é {}Kg e o menor é {}Kg'.format(m, n))
