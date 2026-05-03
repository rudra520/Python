#Program to illustrate the concept of class and objects

#Concepts of class and objects
class Section:
    #Method to display a message
    def __init__(self, name, rollno):
    # name = Yogesh
        self.name = name
        self.rollno = rollno
        print("This is a new student in the section")


#creating objects of the class
s1 = Section("Rohit",45)
print("Name:", s1.name,"and Roll no. :",s1.rollno)
s2 = Section("virat",18)
print(s2.name,s2.rollno)