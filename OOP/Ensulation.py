class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age # private property
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print('enter positive number')
p1=Person('emi', 12)

print(p1.get_age())
p1.set_age(2)
print(p1.get_age())