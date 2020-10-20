from math import *

def my_function():
    groceries = ["milk", "juice", "bread", "cereal", "pop_tarts", "yogurt", "apples", "blue_berries", "oranges", "water", "ice_cream"]
    groceries = str(groceries)
    print("These are the items in your groceries cart: \n" + groceries + ". \n")
    groceries = ["milk", "juice", "bread", "cereal", "pop_tarts", "yogurt", "apples", "blue_berries", "oranges", "water", "ice_cream"]
    item = input("Please enter a item you would like to add to your groceries list: ")
    groceries.append(item)
    groceries.sort()
    groceries = str(groceries)
    print("This is your new list in alphabetical order:\n" + groceries + ". ")

my_function()