a = []
a1 = []
i=1
while i == 1:

    b = input("enter ur number : ( space == exit ) ")
    if b == " ":
        i = 0
    else:
        a.append(int(b))
a1 = sorted(a)

if a1 == a:
    print("ur list is sort", a)
else:
    print("ur list is  not sort", a)




