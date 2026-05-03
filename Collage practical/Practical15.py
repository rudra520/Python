#Program to illustrate the concept of method overriding

#Parent class
class Animal:
    def sound(self):
        print("Animals make some sound")

#Child class overriding the parent method
class Dog(Animal):
    def sound(self):
        print("Dog barks")

#creating objects
a =Animal()
d =Dog()

#Calling methods
a.sound() #Parent class method
d.sound() #Overridden method in child class