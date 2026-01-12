#len() for str
x='hello word'
print(len(x))
#len() for tuple
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))
#len() for dictionary
thisdict={
    'brand':'ford',
    'model':'mustang',
    'year': 1943
    }
print(len(thisdict))


class Vehicle:
    def __init__(self,brand, model):
        self.brand=brand
        self.model=model
    
class Car(Vehicle):
    def Move(self):
        print('drive')
class Boat(Vehicle):
    def Move(self):
        print('sail')
class Plane(Vehicle):
    def Move(self):
        print('Fly')


car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")
for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.Move()

