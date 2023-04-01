# *args = parameter that will pack all arguments into a tuple
#   useful so that a function can accept a varying amount of arguments

def add(*args):
    sum = 0

    for i in args:
        sum += i
    return sum

# *args can be named to something else : for example we use *stuff instead
def sub(*stuff):
    diff = 0
    # values inside the tuple can be manipulated as well by casting it first then changing some values
    stuff = list(stuff)
    stuff[0] = 4

    for i in stuff:
        diff -= i
    return diff


print(add(1,2,3))
print(sub(1,2,3))