# **kwargs = parameter that will pack all arguments into a dictionary
#   useful so that a function can accept a varying amount of keyword arguments

# the kwargs can be replaced with something else, the ** is the only thing that is imporant
#def hello(**kwargs):
def hello(**names):
    print("Hello "+ names['first'] +" "+ names['last'])

    print("Hello ",end=" ")
    for key,value in names.items():
        print(value,end=" ")

hello(title="Mr.",first="wiru",last="mediel",middle="dude")