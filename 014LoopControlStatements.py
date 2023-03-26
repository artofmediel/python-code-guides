# Loop control statements - change a loops execution from its normal sequence
# break, continue, pass

# break     = used to terminate the loop entirely
while True:
    name = input("Enter your name : ")
    if name != "":
        break

# continue  = skips to the next iteration of the loop
phone_num = "123-456-7890"

for i in phone_num:
    if i == "-":
        continue
    print(i, end="")
    # end="" prevents line feed

# pass      = does nothing, acts as a placeholder
for i in range(1,21):
    if i ==13:
        pass
    # skips number 13
    else:
        print(i)
