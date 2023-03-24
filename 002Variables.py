# variable - a container for a value. behaves as the
#           value that it contains

# NOTE:
# type '#' to set line comment

# -----string data type
first_name = 'wiru'
last_name = "uriw"
full_name = first_name + " " + last_name

# display result
print("Hellow " + first_name + ", " + last_name)
print(full_name)

# check data type of variable
print(type(full_name))

# ------int data type
age = 27
print(age)
age += 1

# display
print(age)
print(type(age))

# str to convert datatype to string in order to display
print("your age is " + str(age))

# -----float data type

height = 250.5

print(height)
print("your height is " + str(height) + "cm")
print(type(height))

# -----boolean data type = True or False
nihonjin = False
print(nihonjin)
print(type(nihonjin))
print("you a japanese? " + str(nihonjin))