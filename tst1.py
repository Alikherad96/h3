import random
bank = ["tree", "book", "blue", "trian", "life", "ali", "sky"]
mistake = 0
good_user = []
bad_user = []
x=random.randint(0, len(bank)-1)
w = bank[x]
print(w)

while mistake < 6:
    for i in range (len(w)):
        print("-", end=" ")
    user = input("plz intr ur choice : ")
    if user in w:
        good_user.append(user)
        print("y")
    else:
        bad_user.append(user)
        print("n")
        mistake = mistake + 1

