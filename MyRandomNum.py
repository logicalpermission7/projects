import random
'''
This method will find the lowest and highest integers inside a list
and then subtract the two integers.
'''

def findRange(list):
    lowest = list[0]
    highest = list[0]
    if len(list)==0:
        return -1
    for i in range(len(list)):
        if list[i] < lowest:
            lowest = list[i]
        elif list[i] > highest:
            highest=list[i]
    return highest - lowest



x = range(5, 20, 5)
for i in x:
    print(i)



test = findRange([20,2,3,4,10])

print(test)


aListOfNumbers = [
    [1,4,2,5,3-1],
    [34,-2,-34,9,10],
    [90,56,-11,0],
    [100,99]
]


'''
This method will return the amount of negative numbers inside an array
'''
def countAllNegativeNUmbers(alist):
    num = 0
    for x in alist:
        for y in x:
            if y < 0:
                num += 1
    return num



print(countAllNegativeNUmbers(aListOfNumbers))
