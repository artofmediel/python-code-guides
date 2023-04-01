# Scope = the region that a variable is recognized
#   a variable is only available from inside the region it is created.
#   a global and locally scoped versions of a variable can be created.

#   python follows this hierarchy
#   L = local
#   E = Enclosing
#   G = global
#   B = built-in


name = "mediel"    #global scope (available inside $ outside functions
ign = "goldnugget"

def display_name():
    name = "wiru"   #local scope (available only inside this function)
    #ign = "wiru"   #if removed, the function will get the global value that shares the same name
    print(name)
    print(ign)

display_name()
print(name)
