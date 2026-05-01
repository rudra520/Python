#4.3.3 Effects and results: lists and functions
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s


print(list_sum([5, 4, 3]))

#you should expect problems if you invoke it in this risky way:
print(list_sum(5))



