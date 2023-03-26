# lists = used to store multiple items in a single variable

food = ["pizza","hamburbers","hotdogs","spaghet","breadpudding"]

food[0] = "sushi"

#print(food)
#print(food[0])
#print(food[4])

# append = add item to last index
food.append("ice cream")

# remove = remove an item
food.remove("hotdogs")

# pop remove last item
food.pop()

# insert value at index
food.insert(0,"cake")

# sort alphabetcal
food.sort()

# clear remove all items form the list
#food.clear()

for x in food:
    print(x)