# filter() = creates a collection of elements from an iterable for which a function returns true
#
# filter(function,iterable)

friends = [("Sento",19),
           ("Moffle",28),
           ("Latifa",17),
           ("Macaron",26),
           ("Tiramy",21),
           ("Kanie",28)]

# do lambda function that check age if they can drink : >=18
age = lambda data: data[1]>=18
# use filter function : cast to a list to display
drinking_buddies = list(filter(age,friends))
# display
for i in drinking_buddies:
    print(i)