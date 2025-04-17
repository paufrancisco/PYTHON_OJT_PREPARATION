import pandas as pd

# Create a DataFrame
data = {
    "Item": ["Apple", "Bread", "Milk", "Eggs", "Banana"],
    "Category": ["Fruit", "Bakery", "Dairy", "Dairy", "Fruit"],
    "Price": [2.5, 1.8, 1.2, 2.0, 1.3]
}

df = pd.DataFrame(data)

# Save to an Excel file
df.to_excel("grocery_expenses.xlsx", index=False)
