# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class - a class which contains 1 or more abstract methods.
# abstract method - a method that has a declaration but does not have an implementation

from abc import ABC,abstractmethod

class Vehicle(ABC):

    # the purpose of @abstractmethod is to make sure that all child class
    # that has the Vehicle parent overrides the go and stop method
    # python will prevent the child class to be instantiated
    # if the abstractmethod go and stop is not overriden
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):   # this overrides the abstractmethod go of the Vehicle class
        print("You drive the car")

    def stop(self):
        print("The car is stopped")

class Motorcycle(Vehicle):

    def go(self):   # this overrides the abstractmethod go of the Vehicle class
        print("You ride the motorcycle")

    def stop(self):
        print("The motorcycle is stopped")

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
car.stop()
motorcycle.go()
motorcycle.stop()