import random
while 2 > 1:
    n = int(input("input ur length array : "))
    ar = []
    i = 0
    while i < n:
        a = random.randint(0,10000)
        if ar.count(a) == 0:
            ar.append(a)
            i = i + 1
    print(ar)