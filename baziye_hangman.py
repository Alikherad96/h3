import random


def pprint(n):
    for i in n:
        print(i, end="")
    print()


life = 0
bank = ["book", "red", "blue", "white"]
user = []
wrong = []
wrd = []
l = len(bank)
word = bank[random.randint(0,l-1)]
for i in word:
    wrd.append(i)
#print(word)
for i in range(len(word)):
    print("-", end="")
print()
#tarife araye user ba toole moshakhas
user = ["-" for i in range(len(word))]

while life < 6:
    user_ch = input().lower()
    if len(user_ch) == 1:
        if user_ch in word:
            j = 0
    #bar rasiye vojoode hads dar kalame
            for i in word:
                if user_ch == i and user[j] == "-":
                    user[j] = i
                elif user_ch != i and user[j] == "-":
                    user[j] = "-"
                j += 1
    # def pprint
            pprint(user)
            pprint(wrong)
            if wrd == user:
                print("u win")
                break
        else:
            wrong.append("N")
    #def pprint
            pprint(user)
            pprint(wrong)
            if life == 6:
                print("you lose")
    else:
        print("plz enter one word")