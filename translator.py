def translate(pharse):
    translation = ""
    for letter in pharse:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "Z"
            else:
                translation = translation + "z"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a pharse: ")))



def ask():
    while True:
        try:
            number = int(input("Enter an integer number only: "))
        except ValueError:
            print("invalid entry, not an integer.")
            continue
        else:
            break
    print("good job!")


ask()

grid_list = [
    [1,2,3,4],
    [5,6,7,8],
    [0]
]


for row in grid_list:
    for col in row:
        print(col)


mylist = [10,20,30,40,50,60,70]

number = input("Please enter a number")
mylist.append(number)
mylist.reverse()
print(mylist)

monthConversions = {
    "jan": "january",
    "feb": "February",
    "mar": "March",
}

print(monthConversions["feb"])

count = 0
for letters in "cedjncefjcnfjcnefkcnijrcnrfjcnrcnrijcnrfijcnfrjn":
    count += 1
    print(str(count) + ")" + " " + letters)