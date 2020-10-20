class Dog:
    def __init__(self, type, name, size):
        self.type = type
        self.name = name
        self. size = size

    def is_izzy(self):
        if self.name == "izzy":
            return True
        else:
            return False