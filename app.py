from math import *
# This program was designed to give you the value of your body mass index and tell you weather your underweight, normal, overweight or obeist.
name = input("Enter your name: ")
while True:
    try:
        weight = float(input("Please only enter your weight in pounds " + name + ": "))
    except ValueError:
        print("Invalid entry. Sorry, I didn't understand that.")
        continue
    else:
        break
while True:
    try:
        height = float(input("Now only enter your height in inches " + name + ": "))
    except ValueError:
        print("Invalid entry. Sorry, I didn't understand that.")
        continue
    else:
        break
results = weight / pow(height, 2) * 703
results = round(results)
if results <= 18.5:
    print("Your BMI is " + results + " " + name + ", and you are UNDERWEIGHT.")
elif results >= 18.5 and results <= 24.9:
    results = str(results)
    print("Your BMI is " + results + " " + name + ", and you have a NORMAL BMI.")
elif results >= 25 and results <= 29.9:
    results = str(results)
    print("Your BMI is " + results + " " + name + ", and you are OVERWEIGHT.")
else:
    results = str(results)
    print("Your BMI is " + results + " " + name + ", and you are at OBESITY levels.")
print("\n")
print("Have a nice day " + name + ".")

