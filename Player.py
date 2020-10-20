
'''
This is a class for a player in a game. this class has 2 class functions.
'''
class Player:
    def __init__(self, name, lives, speed, power):
        self.name = name
        self.lives = lives
        self.speed = speed
        self.power = power

    def is_dead(self):
        if self.lives == 0:
            return True
        else:
            return False

    def is_elvis(self):
        if self.name == "elvis" or self.name == "Elvis":
            print("Welcome elvis, you are awesome")
        else:
            print("Welcome new player")

