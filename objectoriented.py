## object oriented programming

# class = 
# objects = instance of a class
# attributes = 
# methods = 


"""
Dog:
    Attributes:
        breed
        weight
        energy

Bilbo Waggins:
breed: labrador
weight: 80lbs
energy: low

"""

class Dog:
    energy = "high"

    def speak(self):
        print("woof")

bilbo_waggins = Dog()

print(bilbo_waggins.energy)
bilbo_waggins.speak()


chewbarka = Dog()
chewbarka.energy = "low"

print(chewbarka.energy)
chewbarka.speak


##############

class Dog:
    def __init__(self, name, breed, energy):
        self.name = name
        self.breed = breed
        self.energy = energy 
dog1 = Dog("Ross Barkley", "Jack Russel", "high")

print(dog1.name)
print(dog1.breed)

###############

_money = 10000



class Feline:
    __family = "Felidae"

kitty = Feline()
print(kitty._Feline__family)


#################

class student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

Kane = student("Kane", "25")
Alia = student("Alia", "20")

print(getattr(Kane, "age"))


##########################

##OOP 

from abc import ABC, abstractmethod

class Bird(ABC):
    fly = True
    babies = 0

    def noise(self):
        return 'Squawk'

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False

class Owl(Bird):

    def reproduce(self):
        self.babies += 6

    def eat(self):
        return "Peck Peck"

class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        return "Nom Nom"

    def reproduce(self):
        if not self.extinct:
            self.babies += 1

Birdie = Dodo()

print(Birdie.Fly)







