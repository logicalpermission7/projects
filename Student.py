class Student:
    def __init__ (self, name, concentration, gpa, is_honors):
        self.name = name
        self.concentration = concentration
        self.gpa = gpa
        self.is_honors = is_honors

    def is_on_honers(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

