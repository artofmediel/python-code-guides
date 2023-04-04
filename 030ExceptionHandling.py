#exception - events detected during execution that interrupt the flw of a program

try:
    numerator =  int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("cant divide by 0")
except ValueError as e:
    print(e)
    print("Number input only")
except Exception as e:
    print(e)
    print("Invalid Input")
else:
    print(result)
finally:
    print("finally block will always execute. use in closing opened file")