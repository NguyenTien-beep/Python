class Outer:
    def __init__(self):
        self.name="Emil"
    class Inner:
        def __init__(self,outer):
            self.name='inner'
            self.outer=outer
        def display(self):
            print('hello from inner class')
            print(f'hello : {self.outer.name}')
            
outer=Outer()
inner=outer.Inner(outer)
inner.display()
        

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self.engine=self.Engine()
    class Engine:
        def __init__(self):
            self.status='Off'
        def start(self):
            self.status='Running'
            print('Engine Started')
        def stop(self):
            self.status='Off'
            print('Engine Stopped')
    def drive(self):
        if self.engine.status =='Running':
            print(f'Driving the {self.brand} {self.model}')
        else:
            print('start the engine first')
car=Car('toyota','corrala')
car.drive()
car.engine.start()
car.drive()


class Computer:
    def __init__(self):
        self.cpu=self.CPU()
        self.ram=self.RAM()
    class CPU:
        def process(self):
            print('Processing data..')
    class RAM:
        def store(self):
            print('Storing data')
            
computer=Computer()
computer.cpu.process()
computer.ram.store()

        