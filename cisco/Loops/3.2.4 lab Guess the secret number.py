secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

user_number = int(input("Enter a Secret Number:-"))
while user_number != secret_number:     
    print("Ha ha! You're stuck in my loop!") 
    user_number = int(input("Enter a Secret Number:-"))
print("Well done, muggle! You are free now.")
