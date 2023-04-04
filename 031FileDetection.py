import os

# path1 = "G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\031Text.txt"
path2 = "G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\031TextFolder"


if os.path.exists(path2):
    print("Location Exists")
    if os.path.isfile(path2):
        print("That is a File")
    elif os.path.isdir(path2):
        print("That is a Directory")
else:
    print("Location not found")