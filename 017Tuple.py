# tuple - collections with are orders and unchangeable
#         - used to group together related data

student = ("Wiru",28,"Male")

print(student.count("Wiru"))

print(student.index("Male"))

for x in student:
    print(x)

if "Wiru" in student:
    print("wiru is here")