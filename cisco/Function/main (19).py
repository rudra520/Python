#4.4 Section 4 – Scopes in Python
#4.4.1 Functions and scopes
def scope_test():
    x=123

scope_test()
print(x)

#It will give you error 

#Let's start by checking whether or not a variable created outside any function is visible inside the functions
def my_function():
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)
#The answer is: a variableexisting outside a function has scope inside the function's body

#making small changes 

def my_function():
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)



.