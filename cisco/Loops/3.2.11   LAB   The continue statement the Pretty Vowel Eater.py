word_without_vowels = ""

# Prompt the user to enter a word
user_word = input("Enter a word: ")

# Convert the word entered by the user to upper case
user_word = user_word.upper()

# Complete the loop body
for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter

# Print the word assigned to word_without_vowels
print(word_without_vowels)