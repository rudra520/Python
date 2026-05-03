#program to find the maximum and minimum numbers in a list

#method 1

numbers = [4, 7, 2, 9, 1, 5]

min_num = numbers[0]
max_num = numbers[0]

for num in numbers:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

print("Maximum number:", max_num)
print("Minimum number:", min_num)


#method 2(using numpy)
numbers =[2,4,5,3]
import numpy
print("Maximum value",numpy.max(numbers))
print("Minimum value",numpy.min(numbers))