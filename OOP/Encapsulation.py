class Student:
    def __init__(self,name):
        self.name=name
        self.__grade=0 #encapsulation
    def set_grade(self,grade):
        if 0 <= grade <= 100:
            self.__grade=grade
        else:
            print('None')
    def get_grade(self):
        return self.__grade
    def get_status(self):
        if self.__grade >=60:
            return 'Passed'
        else:
            return 'False'

student=Student('Emi')
student.set_grade(88)
print(student.get_status())
print(student.get_grade())

class Calculator:
    def __init__(self):
        self.result=0
    def __validate(self,num): # dung de ktra xem input co phai so khong
        if not isinstance(num, (int,float)): # dung de ktra du lieu num
            return False
        return True
    def add(self,num):
        if self.__validate(num):
            self.result += num
        else:
            print('Invalid numver')

calc= Calculator()
calc.add(10)
calc.add(5)
print(calc.result)

class Demo:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
p1=Demo('tien',15)
print(p1.name)
print(p1._Demo__age)

