#Keyword arguments - preceded by an identifier when we pass them to a function
#   The order of the arguments doesn't matter, unlike positional arguments
#   Python knows the names of the arguments that our functions receives

def hello(first,middle,last):
    print("hello "+ first +" "+ middle +" "+ last)

hello(last="wiru",first="mediel",middle="goldnugget")