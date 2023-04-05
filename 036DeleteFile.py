import os
import shutil

#path = "G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\036Text.txt"
#path2 = "G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\036EmptyTextFolder"
path3 = "G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\036TextFolder"


try:
    #os.remove(path2)       # delete a file
    #os.rmdir(path2)        # removedirectory - delete an empty folder
    shutil.rmtree(path3)    # removetree - delete a directory containing files
except FileNotFoundError:
    print("File not Found")
except PermissionError:
    print("You don't have permission to delete that")
except OSError:
    print("You can't delete that using that function")
else:
    #print(path + " was deleted")
    #print(path2 + " was deleted")
    print(path3+" was deleted")