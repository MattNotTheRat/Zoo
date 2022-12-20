from MAIN import *
class Elephant(Animal):
    def __init__(self, name, mass, age):
        self.__biomeToLive = "desert"
        self.__spaceToLive = 0
        self.__foodType = ["banana", "pineapple"]
        self.__isPredator = False
        self.__sound = "tu-tu"
        self.__foodPerDay = 15

        self.__mass = mass
        self.name = name
        self.age = age

    def Eat(self, foodType, mass):
        print(self.name, ":", self.eatSound)
        for a in self.foodType:
            if (a == foodType):
                self.mass += mass

    def MakeSound(self):
        print(self.name, ":", self.sound)

    def Play(self):
        print(self.name, "поиграл ")

    @property
    def mass(self):
        return self.__mass
