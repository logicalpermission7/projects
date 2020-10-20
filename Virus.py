'''
This class is for tracking data on viruses in the world.
The class takes a name, country, infected, deaths, recovered and cure attributes.
It also has 3 class functions that will return data.
'''


class Virus:
    def __init__(self, name, country, infected, deaths, recovered, cure):
        self.name = name
        self.country = country
        self.infected = infected
        self.deaths = deaths
        self.recovered = recovered
        self.cure = cure

    def is_curable(self):
        if self.cure == 1:
            return True
        else:
            return False

    def is_american(self):
        if self.country == "US"or self.country == "us":
            return True
        else:
            return False

    def is_pandemic(self):
        if self.deaths == 500:
            return "pandemic out break"
        else:
            return "not yet high"


