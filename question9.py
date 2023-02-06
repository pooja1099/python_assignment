# oops concept 1:Class and Object
print("oops concept 1:Class and Object")
class Human:
    # class attribute
    species = "Homo Sapiens"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


x = Human("Ron", 15, "Male")
y = Human("Miley", 22, "Female")
print(x.name)
print(y.name)
print(f"Hi! My name is {x.name}. I am a {x.gender}, and I am {x.age} years old")
print(f"Hi! My name is {y.name}. I am a {y.gender}, and I am {y.age} years old")

#oops concept 2: inheritance
# base class
print("oops concept 2: inheritance")
def description(self):
    print(f"Hey! My name is {x.name}, I'm a {x.gender} and I'm {x.age} years old")
#child class

class Boy(Human):    #child class parent class-human()
    def schoolName(self, schoolname):
        print(f"I study in {schoolname}")


b = Boy(x)
b.description()
b.schoolName("Sunshine Model School")

#oops concept 3: Encapsulation
print("oops concept 3: Encapsulation")
class Library:
    def __init__(self, id, name):
        self.bookId = id
        self.bookName = name
        
    def setBookName(self, newBookName): #setters method to set the book name
        self.bookName = newBookName
        
    def getBookName(self): #getters method to get the book name
        print(f"The name of book is {self.bookName}")

        
book = Library(101,"The Witchers")
book.getBookName()
book.setBookName("The Witchers Returns")
book.getBookName()


#oops concept 4: Polymorphism
class Monkey:
    def color(self):
        print("The monkey is yellow in coloured!")

    def eats(self):
        print("The monkey eats bananas!")


class Rabbit:
    def color(self):
        print("The rabbit is white in coloured!")

    def eats(self):
        print("The rabbit eats carrots!")


mon = Monkey()
rab = Rabbit()
for animal in (mon, rab):
    animal.color()
    animal.eats()
#abstraction
print("oops concept 5: abstraction")
from abc import ABC

class Vehicle(ABC):  # inherits abstract class
    #abstract method
    def no_of_wheels(self):
        pass

class Bike(Vehicle):
    def no_of_wheels(self): # provide definition for abstract method
        print("Bike have 2 wheels")  

class Tempo(Vehicle):
    def no_of_wheels(self):  # provide definition for abstract method
        print("Tempo have 3 wheels")
        bike = Bike()
bike.no_of_wheels()
tempo = Tempo()
tempo.no_of_wheels()

