# import pandas as pd
# import os

# # Create a DataFrame
# data = {
#     "Item": ["Apple", "Bread", "Milk", "Eggs", "Banana"],
#     "Category": ["Fruit", "Bakery", "Dairy", "Dairy", "Fruit"],
#     "Price": [2.5, 1.8, 1.2, 2.0, 1.3]
# }

# df = pd.DataFrame(data)

# # Define the full path to the 'day 1' folder
# folder_path = r"C:\Users\ADMIN\Desktop\github\ojt_preparation\ojt_preparation\day 1"

# # Ensure the directory exists, create if not
# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)

# # Save to an Excel file in the specified folder
# file_path = os.path.join(folder_path, "grocery_expenses.xlsx")
# df.to_excel(file_path, index=False)

# print(f"Excel file saved to: {file_path}")


import pandas as pd
import os

#Create a DataFrame

data = {
    "Item" : ["Apple", "Bread", "Milk", "Eggs", "Banana" ],
    "Category" : ["Fruit", "Bakery", "Diary", "Dairy", "Fruit"],
    "Price" : [2.5,1.8,1.2,2.9,1.3]
}

df = pd.DataFrame(data)