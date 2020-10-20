from math import *
import random
from Player import Player
from Student import Student

# This is a "Player Object"
player1 = Player("Elvis", 5, 100, 500)
print(player1.power)
print(player1.is_elvis())

# This is a Student Object
elvis = Student("Elvis", "CSCI", 4.0, True)
print(str(elvis.is_on_honers()) + " is on honers")

# This is a 2d array or "list"
gridList = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19],
    [20],
]

# This is a nested for loop
for row in gridList:
    for col in row:
        print(col)

# This is a Dictionary with 12 Key Value Pairs
monthConversion = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

# This will print out key 2 and its value
print(monthConversion.get(2))

# This will open a file and read from it
file = open("/Users/ironman/Desktop/shakespeare_ai-master/sonnets.txt", "r")
print(file.read())
file.close()

# This will give you a invalid entry unless you type a float, or integer number

while True:
    try:
        number = float(input("Please enter a number: "))
    except ValueError:
        print("Invalid Entry")
        continue
    else:
        break

# This is a function that will return the square root answer to a number
def getSquareRoot(num):
    num = sqrt(num)
    newNumber = round(num)
    return newNumber

# This will print out every individual letter
for letters in "the fox jump ove the big red barn":
    print(letters)


print(getSquareRoot(67))

# this is a list
list = [1,2,3,4,5,6,77,65,45,33,1234,567]

# This will print out the biggest number in the list
print(max(list))
list.reverse()
print(list)
print(list.index(33))







