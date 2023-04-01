# str.format() = optional method that gives users
#   more control when displaying output

animal = "cow"
item = "moon"

#print("The "+ animal +" jumped over the " + item)
#print("The {} jumped over the {}".format("cow","moon"))
print("The {} jumped over the {}".format(animal,item))

#positional argument
print("The {1} jumped over the {0}".format(animal,item))

#keyword argument
print("{human} is cooking a {food}".format(human="wiru",food="pizza"))

text = "The {} jumped over the {}"
print(text.format(animal,item))

name= "wiru"
print("Hello, my name is {}. Nice to meet you!".format(name))
print("Hello, my name is {:10}. Nice to meet you!".format(name))
#left-align for padding
print("Hello, my name is {:<10}. Nice to meet you!".format(name))
#right-align for padding
print("Hello, my name is {:>10}. Nice to meet you!".format(name))
#center-align for padding
print("Hello, my name is {:^10}. Nice to meet you!".format(name))

number = 1000
print("The number pi is {:.3f}".format(number))
print("The number pi is {:,}".format(number))
# display as binary
print("The number pi is {:b}".format(number))
# display as octal
print("The number pi is {:o}".format(number))
# display as hex
print("The number pi is {:X}".format(number)) # uppercase
print("The number pi is {:x}".format(number)) # lowercase
#display as scientific notation
print("The number pi is {:E}".format(number)) # uppercase
print("The number pi is {:e}".format(number)) # lowercase