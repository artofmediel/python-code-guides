
text = "wiru\n123\nmediel\noverwrite text"
text2 = "\ngoldnugget"

# w : write mode
with open('G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\033Text.txt','w') as file:
    file.write(text)

# a : append mode
with open('G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\033Text.txt','a') as file:
    file.write(text2)