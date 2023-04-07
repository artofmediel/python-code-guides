# method chaining = called multiple methods sequentially
#   each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self #this line is needed to fix AttributeError

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You stop the car")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()

# display
car.turn_on().drive()

car.brake().turn_off()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()