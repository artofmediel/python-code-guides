class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("this hawk isi flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()
# test parent
print(rabbit.alive)
fish.eat()
hawk.sleep()
# test child
rabbit.run()
fish.swim()
hawk.fly()