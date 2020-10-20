from math import *
import random
'''
This will find percentage difference between to numbers
'''

#num1 = int(input("Enter a number: "))
#num2 = int(input("Enter another number: "))
#difference = num1 - num2
#total1 = num1 + num2
#totalAverage = total1 / 2
#decimalNum = abs(difference) / totalAverage
#finalPercentage = decimalNum * 100
#print(str(round(finalPercentage)) + "%")

'''
gridList = [
    [1,2,3,4,5,6,],
    [7,8,9,10],
    [11,12,13,14]
]

for row in gridList:
    for col in row:
        print(col)


while True:
    try:
        num = int(input("Enter a number here: "))
    except ValueError:
        print("Invalid Entry")
        continue
    else:
        break

answers = ["Your crazy!", "what if i told you, hell no!", "maybe there is a chance", "when hell freezes over"]

question = input("What is your question to me: ")

print(random.choice(answers))
        

'''

people = ["stranger", "wierdo", "nice person", "cry baby", "soft heart", "You need help"]

question = input("type your name here: ")

print(random.choice(people))

numbers = [100, 34,25,6,7,8,9,12,14]

def sumNumbers(someArray):
    total = 0
    for i in numbers:
        total += i
    print(total)

sumNumbers(numbers)


names = [
    ["elvis", "marvin", "liz", "lennise"],
    ["nolan", "tyler", "mila", "tiffany"],
    ["izzy", "anthony", "kitty", "stacey"]
]

for row in names:
    for col in row:
        print(col, end="---")


pets = ["dog", "cat", "bird", "hamster"]

for i in pets:
    print(i)
