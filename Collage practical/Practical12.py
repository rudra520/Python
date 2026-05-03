# Recursive function to return the nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# Program to print first n fibonacci terms

n = int(input("Enter the number of terms: "))
print("fibonacci series: ")
for i in range(n):
    print(fibonacci(i), end=" ")