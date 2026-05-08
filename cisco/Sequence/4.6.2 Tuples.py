# Tuples prefer to use parenthesis
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125  #it's also possible to create a tuple just from a set of values separated by commas.

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

# Don't try to modify a tuple's contents! It's not a list!

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)


# count() method
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # outputs: 4


# program that will convert the my_list list to a tuple
my_list = ["car", "Ford", "flower", "Tulip"]

t = tuple(my_list)
print(t)

# convert the colors tuple to a dictionary.
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)