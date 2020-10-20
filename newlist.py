
# This is a list and a nested for loop. This will print out every item seperate in the list

'''
This is just practice and for fun!
'''

grid_lsit = [
    ["Apple", "Bannana", "Cherries", "Donuts"],
    ["Eggos", "Fish", "Grapes", "Ham", "ice"],
    [1,2,3,4,5,6,7,8,9],
]

for row in grid_lsit:
    for col in row:
        print(col)

new_list = []

name = input("Enter your name: ")
new_list.append(name)
print(new_list)

print(pow(3,7))

def power(num1, num2):
    results = pow(num1,num2)
    print(results)

power(3,78)

# This is a tuple list
coordinates = (12,45)

monthConversion = {
    "jan": "January",
    "feb": "February",
    "mar": "march",
}

print(monthConversion.get("feb"))

groceries = ["cdekcnw", "wdnccnc", "wdcnenwn"]

for row in groceries:
    groceries.sort()
    print(row)

count = 0
for letters in "ecwdnciowhnocnwocnwkncwoifnwkfnwofnriufn3rjnwdfnwkjcbnwocnwlnkcnwocbn":
    count += 1
    print(str(count) + ")" + " " + letters)