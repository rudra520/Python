#Here i define Function name num.
def num():# this is first part of function in which we define fuction
    input_num = int(input("Enter a number: ")) # this is part second  in which we define statment 
    if input_num % 2 == 0:
        print("The number is even.")    
    else:
        print("The number is odd.")
      # here we invoking function.
print("This program determines if a number is even or odd.")
num()
