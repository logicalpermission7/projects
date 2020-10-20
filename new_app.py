from Student import Student
from Iphone import Iphone
from Elvis import Elvis
from Vehicle import Vehicle
from Questions import Questions
from math import *
import random


'''
This is just some practice code, so that I can get good at it.
If you want to help with this code then just apple at codewithelvis.com
good bye!
'''

vehicle1 = Vehicle("car", "black", 450 )


student1 = Student("elvis", "CSCI", 3.5, True)
print(student1.name)

student2 = Student("tiffany", "nursing", 4.0, True)

phone_1 = Iphone(8, "black", 256, "plus" )
phone_2 = Iphone(7, "silver", 800, "regular")

brazil = Elvis(74, 240, 1979, "brazil", "steak", 'dog', False, "scientist",)

print(brazil.birth_place)
print(vehicle1.max_speed)

question_prompts = [
    "What is your name:  \n a) Tommy\n b) Smith\n c) Elvis\n d) Jessica\n\n",
    "What city do you live in:  \n a) New York\n b) Clarksville\n c) Chicago\n d) Boston\n\n ",
    "What color are strawberries: \n a) Red\n b) Black\n c) White\n d) They have no color\n\n",

]

questions = [
    Questions(question_prompts[0], "c"),
    Questions(question_prompts[1], "b"),
    Questions(question_prompts[2], "a"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct!")

run_test(questions)

