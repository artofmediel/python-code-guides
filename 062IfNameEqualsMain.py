# *************************
# if __name__ == '__main__'
# *************************

# the main purpose of this code is it allows modules to have some flexibility


# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if it's
# the initial module being run.
# then Python will execute the code found within __main__

# put this code in module_two.py
# import module_two
# print(__name__)
# print(module_two.__name__)


# put this code in module_one.py
if __name__ == '__main__':
    print("running this module directly")
else:
    print("running other module indirectly")

