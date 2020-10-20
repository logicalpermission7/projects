from math import *
import random

def how_old_are_you():

    this_year = 2020
    legal_age = 21
    name = input("What is your first name: ")
    while True:
        try:
            year = int(input("What year was you born in " + name + ": "))
        except ValueError:
            print("Invalid entry " + name + ", Please try again: ")
            continue
        else:
            break
    age = this_year - year
    if age < legal_age:
        age = str(age)
        print("You are " + age + " " + name + " and cannot purchase any beer or firearms.")
    else:
        age = str(age)
        print("You are " + age + " years old " + name + ". Go get you some beer and some guns.")

how_old_are_you()


