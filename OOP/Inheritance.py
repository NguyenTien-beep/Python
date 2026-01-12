class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
    def __init__(self,fname, lname,year):
        #Person.__init__(self,fname,lname)
        super().__init__(fname,lname) # dung super() thay vi dung goi la parent' class
        self.graduationyear=year
    def welcome(self):
        print('welcome', self.firstname, self.lastname, 'to the class of',self.graduationyear)
        
x= Student('tien','jason',2025)
print(x.firstname)
print(x.welcome())