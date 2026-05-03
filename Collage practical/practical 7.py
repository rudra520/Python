string = input("Enter a string: ")
char = input("Enter the character to find frequency: ")

count = 0

for i in string:
    if i == char:
        count += 1

print("Frequency of", char, "is:", count)

print("program done by Vipul Rastogi")