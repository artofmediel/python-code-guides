# dictionary = A changeable, unordered collection of unique key:value pairs
#   Fast because they use hashing, allowing us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

# update or add
capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
# removing items
capitals.pop('China')
#capitals.clear()

print(capitals['Russia'])

print(capitals.get('Germany'))

print(capitals.keys())

print(capitals.values())

print(capitals.items())

for key,value in capitals.items():
    print(key,value)