import random
from math import *

my_list = ["You will have sleep problems tonight", "You will have a good night sleep", "go see a doctor about your sleep", "Do not go to sleep tonight"]
name = input("Enter your name here: ")
answers = random.choice(my_list)
str(answers)
print(name + " " +answers)