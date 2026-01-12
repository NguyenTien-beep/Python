class Myclass:
    x=5

p1= Myclass()
print(p1.x)


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person('Emi',36)
print(p1.name)
print(p1.age)

class Person1:
    def __init__(self,name,age=18):
        self.name=name
        self.age=age
    def greet(self):
        print('Hello, My name is' + self.name)
    def printname(self):
        print(self.name)

p1=Person1('Emi')
p2=Person1('Thonny',25)
print(p1.name, p1.age)
p1=Person1('emi',25)
p1.greet()
print(p2.name, p2.age)
p1.printname()

class Car:
    def __init__(self, brand, model, year):
        self.brand=brand
        self.model=model
        self.year=year
    def display_info(self):
        print(f'{self.brand} {self.model} {self.year}')
car1= Car('toyota','corolla',2020)
car1.display_info()

class Person1:
    def __init__(self,name, age):
        self.name=name
        self.age=age
    def greet(self):
        return 'hello, ' + self.name
    def welcome(self):
        message = self.greet()
        print(message + '! welcome to our website')
p1=Person1('class',26)
p1.welcome()

print(p1.age)
p1.age= 36
print(p1.age)
del p1.age
print(p1.name)


class Person:
    species ='Human'
    lastname=''
    def __init__(self,name):
        self.name=name
print('start')
p1=Person('emil')
p2=Person('tobias')
Person.lastname='tien'
print(p1.lastname)
print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)
p1.city='HCM'
print(p1.city)

#Methods


