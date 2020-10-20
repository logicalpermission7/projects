from math import *
import random

def square_root(number):
    number = sqrt(number)
    number = str(number)
    print("The square root is: " +  number)
square_root(25)


def power_of(num1, num2):
    results = pow(num1, num2)
    results = round(results)
    print(str(num1) + " to the power of " + str(num2) + " = " + str(results))
power_of(235, 3)


def  alist():
    coordinates = (4,6)
    print(coordinates)

alist()

def myfunction():
    mylist = ["apple", "oranges", "bananas", "grapes", "watermelon" ]
    item = input("Please add your fruit to the list: ")
    mylist.append(item)
    mylist.sort()
    str(mylist)
    print(mylist)
myfunction()


def sayhello():
    mylist = ["asshole", "dip shit", "fuck face", "awesome person", "loser"]
    name = input("Please enter your name: ")
    message = random.choice(mylist)
    print("Hello " + name + " your a " + str(message) + ".")
sayhello()


def lottery():
    numbers = [0,1,2,3,4,5,6,7,8,9,10]
    numbers = random.choice(numbers)
    print(str(numbers))
lottery()


def cube(num):
    return num * num * num

print(cube(5))




