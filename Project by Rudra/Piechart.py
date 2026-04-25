import pandas as pd
import matplotlib.pyplot as plt

print("=== Pie Chart Generator ===")
print("Enter your categories and sizes.\n")

categories = []
sizes = []

while True:
    print(f"--- Entry {len(categories) + 1} ---")
    
    category = input("Enter category name (or 'done' to finish): ").strip()
    
    if category.lower() == 'done':
        if len(categories) < 2:
            print("Please enter at least 2 categories!\n")
            continue
        else:
            break
    
    if not category:
        print("Category name cannot be empty!\n")
        continue
    
    while True:
        try:
            size = float(input(f"Enter size/value for '{category}': "))
            if size <= 0:
                print("Size must be a positive number!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    categories.append(category)
    sizes.append(size)
    print(f"✓ Added: {category} = {size}\n")

# ---- Build DataFrame ----
data = {'Categories': categories, 'Sizes': sizes}
df = pd.DataFrame(data)
df.set_index('Categories', inplace=True)

# ---- Ask for chart title ----
title = input("\nEnter chart title (or press Enter for default): ").strip()
if not title:
    title = "My Pie Chart"

# ---- Plot ----
fig, ax = plt.subplots(figsize=(8, 6))

df.plot.pie(
    y='Sizes',
    ax=ax,
    autopct='%1.1f%%',
    startangle=140,
    legend=False
)

ax.set_ylabel('')
plt.title(title, fontsize=16, fontweight='bold')
plt.tight_layout()

print("\n✅ Chart generated! Close the chart window to exit.")
plt.show()