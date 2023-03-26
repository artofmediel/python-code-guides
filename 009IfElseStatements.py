age = int(input("How old are you? : "))

# NOTES:
# careful with the indentation
# order of condition statements matters
# -the first condition that is detected as valid will execute and skip over the succeeding conditions whether they're true or not

if age == 100:
    print("You are a century old.")
elif age >= 18:
    print("You are an adult.")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("You are a child.")