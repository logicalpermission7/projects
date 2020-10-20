from Kia import Kia
from math import *
import random
from Dog import Dog
import pandas as pd



mydog = Dog("shepard", "izzy", "large")

mydog.is_izzy()

print(mydog.name)


van1 = Kia("sedona", True, "blue", 8)

myfile = open("/Users/ironman/Desktop/python_class.txt", "r")

print(myfile.readable())

print(myfile.read())

myfile.close()

gridlist = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,12,14],
    [0]
]
count = 0

for letters in "wcgwcbwwecwhcwhcwncwhxwchwhw":
    print(letters)

df = pd.read_csv("/Users/ironman/Desktop/transactions.CSV")
print(df)

valuelist = [1,3,3,4,5,6,7]
for value in valuelist:
    if value == 3:
        print(str(value) + " " + "HERE IT IS!")
    else:
        print(str(value) + " " + "false")

def sayGreeting():
    name = input("Enter your name: ")
    print("Hello " + name)



greetingDictionary = {
    1: sayGreeting(),
    2: "Hello dude",
    3: "Whats up"
}


print(greetingDictionary.get(1))

'''
this part creates a file and allows you to write and read to it.
'''

def questions():

    notes = input("What would you like to say: ")
    saveProgram = input("Type \"y\" to save file: ")
    if saveProgram == "y" or saveProgram == "Y":
        newfile = open("/Users/ironman/Desktop/new.txt", "w")
        print(newfile.write(notes.strip().title()))
        newfile.close()
        print("File Saved...")

    else:
        print("File Closed...")


questions()


myDictionary = {
    1: questions(),
    2: sayGreeting(),
    3: "hello world",
}


theGridList = [
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18],
    [19,20]
]

for row in theGridList:
    for col in row:
        print(col, end="")


