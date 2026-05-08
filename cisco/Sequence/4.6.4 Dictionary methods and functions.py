# The keys() method
#  adapt any dictionary to the for loop requirements
# The first of them is a method named keys(), possessed by each dictionary. The method returns an iterable object consisting of all the keys gathered within the dictionar
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

# Let's now have a look at a dictionary method called items(). The method returns tuples (this is the first example where tuples are something more than just an example of themselves) where each tuple is a key-value pair.

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)

# Modifying and adding values
# replace the value "chat" with "minou",
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou'
print(dictionary)

# sorted
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in sorted(dictionary.keys()):
    print(key)

# There is also a method called values(), which works similarly to keys(), but returns values.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for french in dictionary.values():
    print(french)
    
# Adding a new key
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['swan'] = 'cygne'
print(dictionary)

# You can also insert an item to a dictionary by using the update() method
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.update({"duck": "canard"})
print(dictionary)

# Removing a key
# Note: removing a key will always cause the removal of the associated value. Values cannot exist without their keys.

# This is done with the del instruction.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

del dictionary['dog']
print(dictionary)

# To remove the last item in a dictionary, you can use the popitem() method:
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.popitem()
print(dictionary)    # outputs: {'cat': 'chat', 'dog': 'chien'}

