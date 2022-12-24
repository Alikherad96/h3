print(" in barname tamame ja khaliha ra shenasayee mikonad")
while 2>1:
    a = input("enter ur sentence :")
    c = 0
    for i in range(len(a)-1):
        if len(a) > i:
            if a[i] != " " and a[i+1] == " ":
                c += 1
    if a[len(a)-1] != " ":
        c +=1
    print("tedade carktere jomleye shoma : = ", c)
