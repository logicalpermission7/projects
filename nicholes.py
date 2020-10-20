import random
from math import *
from taxes import money


subject1 = money(123, 34)

subject1.isLow()



name = input("Enter the name of your cat please: ")
while True:
    try:
        age = int(input("Enter the age of your cat: "))
    except ValueError:
        print("Invalid entry")
        continue
    else:
        break


def getSquareRoot(num):
    num = sqrt(num)
    print(round(num))


getSquareRoot(34)

gridlist = [
    [1,2,3,4,5],
    [5,7,8,9,10],
    [11,12,13,14,15]
]

for row in gridlist:
    for col in row:
        print(col)

count = 0
for letters in "efcjefhcoiuefhcejcehcejbcekjcnefiucnefcbecbjibcjef":
    count += 1
    print(str(count) + ")" + " " + letters)