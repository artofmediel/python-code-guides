# index operator [] = give access to a sequence's element
#                       (str,list,tuples)

name = "wiru GOLDNUGGET!"

if(name[0].islower()):
    name = name.capitalize()
print(name)

# remember string slicing
first_name = name[:4].upper()
print(first_name)

last_name = name[5:].lower()
print(last_name)

#last_character = name[-1]
last_character = name[-2]
print(last_character)