class money:
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2


    def isLow(self):
        if self.num1 < 100:
            return True
        else:
            return False

