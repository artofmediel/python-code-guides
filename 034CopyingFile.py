# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\034Text.txt','G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\034TextCopy.txt') #src,destination