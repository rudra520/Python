# program to find the average value in a list

#Method 1
A = [2, 4, 6, 8]
value = 0

for num in A:
    value += num
    
count= len(A)
avg =value / count       
print(avg)  

#method 2 (using numpy)

numbers=[2,4,6,8,]
import numpy
print("Average",numpy.average(numbers))