def hello():
    print("Hello")

# display memory address of the function
#print(hello)
# assign same memory to variable hi
#hi = hello
# display to check if both are same address
#print(hi)

# assign same memory to variable hi
hi = hello
# test if hi will do same function as hello
hello()
hi()

# -------------------------
# try doing this with the print() function: name the variable say
say = print
# test
say("wiru 123 123")
