# # Prompt the user to enter a word
# user_word = input("Enter a word: ")

# # Convert the word to upper case
# user_word = user_word.upper()

# # Complete the body of the for loop
# for letter in user_word:
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#     else:
#         print(letter)

# Short Meathod

# Prompt the user to enter a word
user_word = input("Enter a word: ")

# Convert the word to upper case
user_word = user_word.upper()

# Complete the body of the for loop
for letter in user_word:
    if letter in ("A","O","U","I","E"):
        continue
    else:
        print(letter)
        


