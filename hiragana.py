import random
from data import Hiragana, CompareHandK
selects = []
after_select = []


while True:
    select = input("Input : ").lower()
    if select == "0":
        break
    if select in selects:
        continue
    else:
        selects.append(select)

def shuffle_latter(i):
    getlatter = Hiragana[i]
    random.shuffle(getlatter)  
    return getlatter  

for i in selects:
    for j in shuffle_latter(i):
        after_select.append(j)

for i in after_select:
    user = input(f"{i} Input Your guess : ").lower()
    if CompareHandK[user] == i:
        print("You right")
    else:
        print("You wrong")
print(after_select)
print(selects)