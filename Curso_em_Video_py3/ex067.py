while True:
    print('-=-'*11)
    n = int(input('Tabuada de...:\t'))
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n}\tX\t{i}\t=\t{n*i}')
