print("bmm program ( space == exit )")
while 2 > 1:

    aa = input("first number : ")
    if aa == " ":
        break
    else:
        a = int(aa)
        b = int(input("second number : "))
        for i in range(a):
            i += 1
            if (a % i == 0) and (b % i == 0):
                c = i

        print("bmm = ", c)