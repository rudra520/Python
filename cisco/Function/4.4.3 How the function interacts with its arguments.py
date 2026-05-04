def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)
# The conclusion is obvious ‒ changing the parameter's value doesn't 
# propagate outside the function (in any case, not when the variable is a scalar, like in the example).

var = 1
my_function(var)
print(var)


# another example 

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

# another example 

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

# Can you explain it?

# Let's try:

# if the argument is a list, then changing the value of the corresponding parameter doesn't affect the list (remember: variables containing lists are stored in a different way than scalars)
# but if you change a list identified by the parameter (note: the list, not the parameter!), the list will reflect the change.

