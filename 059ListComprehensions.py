# list comprehension = a way to create a new list with less syntax
#                   can mimic certain lambda functions, easier to read
#                   list = [expression for item in iterable]
#                   list = [expression for item in iterable if conditional]
#                   list = [expression (if/else) for item in iterable]

# create a program that list all the numbers 1 - 10 squared
squares = []                # create an empty list
for i in range(1,11):       # create a for loop
    squares.append(i * i)   # define what each loop iteration should do
print(squares)

# can be coded like this
# list = [expression for item in iterable]
squares = [i * i for i in range(1,11)]
print(squares)

# ------------------------
# mimic a lambda function

students = [100,90,80,70,60,50,40,30,0]

passed_students = list(filter(lambda x: x>=60,students))

print(passed_students)

# can be coded like this
# list = [expression for item in iterable if conditional]
passed_students_new = [i for i in students if i >= 60]
print(passed_students_new)

# -----------------------

# list = [expression( if / else ) for item in iterable]
passed_students_new_list = [i if i >= 60 else "FAILED" for i in students]
print(passed_students_new_list)