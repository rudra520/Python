# Function to show different types of arguments
def multiply(a,b=5):
    print("a =",a)
    print("b =",b)
    print("Result =",a*b)

print("Positional Arguments:")
multiply(4,3)   # a=4 ,b=3

print("Default Argument:")
multiply(7)    # it will take b=5 as default value

print("Keyword Arguments:")
multiply(b=10,a=2)    # Here we are taking new values