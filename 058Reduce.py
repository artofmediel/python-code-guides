# reduce() = apply a function to an iterable and reduce it to single cumulative value.
#          performs function on first two elements and repeats process until 1 value remains
#
# reduce(function,iterable)

import functools

letters = ["H","E","L","L","O"]

word = functools.reduce(lambda x,y,:x+y,letters)
# "H","E","L","L","O"
# "HE","L","L","O"
# "HEL","L","O"
# "HELL","O"
# "HELLO"
print(word)
# ------------------------
factorial = [5,4,3,2,1]

result = functools.reduce(lambda x,y,:x*y,factorial)
# 5,4,3,2,1
# 20,3,2,1
# 60,2,1.
# 120,1
# 120
print(result)
