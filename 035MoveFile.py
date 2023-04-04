import os

# test :  move file
source = "G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\035Text.txt"
destination = "G:\\William\\\python-projects\\PycharmProjects\\PythonTestFiles\\035DestinationFolder\\035Text.txt"

# test :  move folder
source2 = "G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\035Folder"
destination2 = "G:\\William\\\python-projects\\PycharmProjects\\PythonTestFiles\\035DestinationFolder\\035Folder"

# Test :  move a file to a test destination folder
# Test :  move a folder to a test destination folder

try:
    if os.path.exists(destination2):
        print("File already exist")
    else:
        os.replace(source2,destination2)
        print(source2 + "was moved")
except FileNotFoundError:
    print(source2 + " was not found")