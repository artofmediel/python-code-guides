# set = collection which is unordered, unindexed, no duplicates values

utensils = {"fork","spoon","knife","knife"}
dishes = {"bowl","plate","cup","knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()

# adds items of dishes to utensils
#utensils.update(dishes)

dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x)

print(utensils.difference(dishes))
print(dishes.difference(utensils))

print(utensils.intersection(dishes))
