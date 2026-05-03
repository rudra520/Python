num = int(input("Enter a number: "))
temp = num
total_sum = 0

total_digits_or_powers = len(str(num))

while temp > 0:
    digit = temp%10
    total_sum += digit**total_digits_or_powers
    temp//= 10 

if num == total_sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
    
print("program done by Vipul Rastogi")