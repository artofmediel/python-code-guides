
try:

    #with open('G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\032Text.txt') as file:
    # test file not found
    with open('G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\032Text.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("That file is not found")

# check if file is closed ; opened file is closed automatically
#print(file.closed)