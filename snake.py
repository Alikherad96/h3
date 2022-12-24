a = int(input("snake len : "))
i = 0
for i in range(int(a/2)):
    print("*#", end="")
if a % 2 != 0:
    print("*", end="")
