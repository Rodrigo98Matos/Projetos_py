def maior(* num):
    m = 0
    for i, n in enumerate(num):
        if i == 0:
            m = n
        elif n > m:
            m = n
    print(m)


maior(1,2,5,65,1)
maior()
