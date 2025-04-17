print("Input the prices of 5 grocery items and display the total")

container = 0

for i in range(1,6):
    grocery = int(input(f"{i} grocery: "))
    container += grocery
    
print(f"The sum of the expenses: {container}")