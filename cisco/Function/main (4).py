#4.3.2 A few words about None
value = None
if value is None:
    print("Sorry, you don't carry any value")
#Don't forget this: if a function doesn't return a certain value using a return expression clause, it is assumed that it implicitly returns None.

def strange_function(n):
    if(n % 2 == 0):
        print("Even")
        return True

strange_function(4)
