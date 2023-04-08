# Higher Order Function = a function that either
#                       1. accepts a function as an operator
#                       or
#                       2. returns a function
#                       (In python, functions are also treated as objects)

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

# this is the higher order function
def hello(func):
    text = func("Hello")
    print(text)

# this will print HELLO because loud function is passed into the function hello
hello(loud)
# this will print hello
hello(quiet)

# ------------------------

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

# pass 2 to be x value :
# dividend function is skipped(not yet called):
# return dividend and assign x value to a variable(divide)
# we can call a variable if it has the memory address of a function
divide = divisor(2)
# now call dividend and pass in 10 as y value
# y = 10 : x = 2
# print result
print(divide(10))