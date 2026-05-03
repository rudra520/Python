

print("1. Right Triangle Pattern:")
rows = 5
for i in range(1, rows + 1):
    print("*" * i)

print("\n2. Inverted Triangle Pattern:")
for i in range(rows, 0, -1):
    print("*" * i)

print("\n3. Pyramid Pattern:")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

print("\n4. Square Pattern:")
for i in range(rows):
    print("* " * rows)

print("\n5. Number Triangle:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


print("program done by Vipul Rastogi")