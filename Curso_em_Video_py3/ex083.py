abre = list()
e = str(input("Digite um expressão:\t")).strip()
for p in e:
    if p in '({[':
        abre.append(p)
    if p == ')':
        if len(abre) != 0 and abre[-1] == '(':
            abre.pop()
            exp = True
        else:
            exp = False
            break
    elif p == '}':
        if len(abre) != 0 and abre[-1] == '{':
            abre.pop()
            exp = True
        else:
            exp = False
            break
    elif p == ']':
        if len(abre) != 0 and abre[-1] == '[':
            abre.pop()
            exp = True
        else:
            exp = False
            break
if exp and len(abre) == 0:
    print("\033[32mExpressão correta!\033[m")
else:
    print("\033[31mExpressão errada!\033[m")
