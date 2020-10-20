import random



def get_password():
    characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "&", "*", "q", "w", "e",
                  "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h",
                  "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
                  "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X","C", "V", "B", "N", "M", "_", "-", "{", "]", "["]
    while True:

        try:

            length = int(input("Enter a number 6 or greater for the length: "))


        except ValueError:
            print("invalid entry, only numbers 6 or greater")
            continue
        else:
            if length < 8:
                length = 0
                get_password()
        for times in range(0,length):
            print(' '.join(random.choices(characters)), end="")

        break




get_password()

