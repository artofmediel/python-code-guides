# slicing = create a substring by extracting elements from another string
#       indexing[] or slice()
#       [start:stop:step]

name = "wiru william"

first_name = name[:3]
#leaving the first condition(start) being blank, would automatically read by python as 0 value#leaving the first condition(start) being blank, whould automatically read by python as 0 value

last_name = name[4:]
#leaving the second condition(stop) being blank, would automatically read by python as 0 value, and print the rest of the string starting from the start index

funky_name = name[::3]

reversed_name =name[::-1]


print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

# ----------------------------

website1 = "http://google.com"
website2 = "http://wikipedia.com"

#separate conditions with comma ',' instead of colon ':'
slice = slice(7,-4)

print(website1[slice])
print(website2[slice])
