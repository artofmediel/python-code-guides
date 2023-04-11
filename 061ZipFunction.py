# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets,etc.)
#                   creates a zip object with paired elements stored in tuples for each elements


usernames = ["wiru","dude","mediel"]
passwords = ("p@ssword","abc123","guest")

users = zip(usernames,passwords)
# check class type of zip
print(type(users))

for i in users:
    print(i)

users = list(zip(usernames,passwords))
# zips can be cast to list
print(type(users))

users = dict(zip(usernames,passwords))
# zips can be cast to list
print(type(users))

for key,value in users.items():
    print(key+" : "+value)

# ---------------------------------
# you can add more iterable

login_date = ["1/1/2021","1/2/2021","1/3/2021"]

users_new = zip(usernames,passwords,login_date)

for i in users_new:
    print(i)

