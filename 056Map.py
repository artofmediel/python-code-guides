# map() = applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)

# example : convert prices of items in the list of tuples from dollar to euro
store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_euros = lambda data: (data[0],data[1]*0.82) #  1 dollar = 0.82 euro

store_euros = list(map(to_euros, store)) # use the map function : cast it to list to display result
# display
for i in store_euros:
    print(i)

# convert back to dollars
to_dollars = lambda data: (data[0],data[1]/0.82) #  divide to turn it back to dollar value
# use map function : cast to list
store_dollars = list(map(to_dollars, store))
# display
for i in store_dollars:
    print(i)
