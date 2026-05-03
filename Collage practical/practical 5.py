num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative number")
elif(num == 0 or num == 1):
    print("Factorial of", num, "is",factorial)
else:
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "is", factorial)


print("program done by Vipul Rastogi")
