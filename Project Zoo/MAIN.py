
class Animal:
    def __init__(self, name, mass, age):
        self.biomeToLive = ""
        self.spaceToLive = 0
        self.foodType = ["",""]
        self.isPredator = False
        self.sound = ""
        self.mass = 0

        self.eatSound = "Om-Nom-Nom"

        self.name = name
        self.foodPerDay = 0
        self.age = age

    def Eat(self, foodType, mass):
        print(self.name, ":", self.eatSound)
        for a in self.foodType:
            if (a == foodType):
                self.mass += mass

    def MakeSound(self):
        print(self.name, ":", self.sound)

    def Play(self):
        print(self.name, "поиграл")


    @property
    def mass(self):
        return self.__mass

    @property
    def isFeeded(self):
        return self.__isFeeded