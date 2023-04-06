# multiple inheritance - when a child class is derived from more than 1 parent class

class Prey:
    def flee(self):
        print("This animal fleed")
class Predator:
    def hunt(self):
        print("This animal hunts")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()

fish.flee()
fish.hunt()