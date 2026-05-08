# The dictionary is another Python data structure. It's not a sequence type (but can be easily adapted to sequence processing) and it is mutable.
# How to make a dictionary

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}  #(keys → numbers, values → strings) 
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

# The list of pairs is surrounded by curly braces, while the pairs themselves are separated by commas, and the keys and values by colons.


# How to use a dictionary
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

# Print the values here.
print(dictionary['cat'])
print(phone_numbers['boss'])
print(empty_dictionary)

#  you mustn't use a non-existent key
#  The in operator, together with its companion, not in, can salvage this situation.

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")
# programmer-friendly
# This kind of formatting is called a hanging indent.
# Example 1:
dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
}
# Example 2:
phone_numbers = {'boss': 5551234567,
              'Suzy': 22657854310
}




