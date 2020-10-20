class Elvis:
    def __init__(self, height, weight, birth_year, birth_place, favorite_food, pet, is_married):
         self.height = height
         self.weight = weight
         self.birth_year = birth_year
         self.birth_place = birth_place
         self.favorite_food = favorite_food
         self.pet = pet
         self.is_married = is_married

    def whatPet(self):
        if self.pet == "izzy":
            print("thats cool")
        else:
            print("Get a new dog")


