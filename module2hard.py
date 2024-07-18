for i in range(3, 21):
    x = ''
    for j in range(1, i):
        for k in range(1, i):
            if i % (j + k) == 0:
                if str(k) not in x:
                    x = x + str(j) + str(k)



    print(i, '-', x)