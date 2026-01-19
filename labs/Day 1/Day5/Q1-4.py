#single
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")


# Object creation
c = Car()
c.start()
c.drive()


#multilevel
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")


# Object creation
e = ElectricCar()
e.start()
e.drive()
e.charge()
