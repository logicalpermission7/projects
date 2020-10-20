class Kia:
    def __init__(self, model, is_awd, color, passenger_size):
        self.model = model
        self.is_awd = is_awd
        self.color = color
        self.passenger_size = passenger_size

    def is_all_wheel_drive(self):
        if self.is_awd:
            return True
        else:
            return False

