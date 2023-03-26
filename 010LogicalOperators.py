# Logical Operators - and or not

temp = int(input("What is the temperature outside? : "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today.")
    print("Go outside.")
elif temp < 0 or temp > 30:
    print("The temperature is bad today.")
    print("Stay inside.")

# not(condition/s)

if not(temp >= 0 and temp <= 30):
    print("The temperature is good today.")
    print("Go outside.")
elif not(temp < 0 or temp > 30):
    print("The temperature is bad today.")
    print("Stay inside.")