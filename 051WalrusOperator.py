# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

happy = True
print(happy)
# can be like this
print(happy := True)

# ------------------------

# Practical use : a program that lets user input values to store in a list
#               with condition that quit stops the loop
#foods = list()
#while True:
#    food = input("What food do you like? : ")
#    if food == "quit":
#        break
#    food.append(food)

# It can be simplified to be like this
foods = list()
while food := input("What food do you like? : ") != "quit":
    foods.append(food)
