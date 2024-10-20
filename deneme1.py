# class deneme1:

#     def __init__(self,ad,soyad):
#         self.ad = ad
#         self.soyad = soyad

# kullanici1 = deneme1("hulusi","demir")

# print(kullanici1.ad) 
# print(kullanici1.soyad) 

# ######################
    
# class deneme2:
#     pass

# kullanici2 = deneme2()

# kullanici2.ad = "hulusi"

# kullanici2.soyad = "demir"

# print(kullanici2.ad)
# print(kullanici2.soyad)

class Person(object):
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# Child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # Invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

# Creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# Calling a function of the class Person using its instance
a.display()
