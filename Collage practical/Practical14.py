#Program to illustrate the concept of inheritance 

#Concept of inhertiance
#parents/base/super class
class Animal:
    def sound(self):
        print("Animals make different sounds")

#chil/derived/sub class inherting from animal
class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof Woof!")


#Creating object of child class
d = Dog()

#Calling parent class method using child object
d.sound()

#Calling child class method
d.bark()