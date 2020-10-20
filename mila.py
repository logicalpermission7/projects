from math import *
import random


grid_list = [
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18],
    [20,21,22,23,24,25],
]

monthConversion = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
}

x = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

print(x.get("a"))


def letters():
    number = 0
    for letters in "efjcnefcjoenbcoencejncfcknfecencekcnfecknefconewcmndcoencledsncekcnk":
        number += 1
        print(str(number) + ")" + " " + letters)


letters()


