# lambda function - function written in 1 line using lambda keyword
#                  - accepts any number of arguments, but only has one expression
#                  (think of it as a shortcut)
#                  (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

# example
#def double(x):
#    return x * 2

# this can be turned into this
double = lambda x: x*2
# test
print(double(5))

# -------------------
# other examples
multiply = lambda x, y: x * y
print(multiply(5,6))

add = lambda x, y, z: x + y + z
print(add(5,6,7))

full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("wiru","123"))

age_check = lambda age: True if age >= 18 else False
print(age_check(12))
print(age_check(18))