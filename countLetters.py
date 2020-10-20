from colored import fg,bg, attr
import random

'''
This short program will count the letters in the words and only print those that are greater then 14
'''
words = ["elephant","monkey","buildings","people"]
color = fg('green')

for count in words:
    if len(count) > 14:
        bigWord = ("This word " + count.upper() + " has more then 14 letters in it.")
        print(bigWord)
    elif len(count) < 14:
        bigWord = ("Nothing here")
        print(color + bigWord)
i = 1
while (i < 256):
    color = fg(i)
    print(color + "All the colors of the rainbow" )
    i += 1

