# day2_exercises.py

# 1️⃣ Variables and Printing
name = "Paulo"
age = 21
favorite_color = "Blue"
print("Name:", name)
print("Age:", age)
print("Favorite Color:", favorite_color)

# 2️⃣ User Input
name = input("What's your name? ")
age = input("How old are you? ")
hobby = input("What’s your hobby? ")
print("Nice to meet you,", name)
print("You're", age, "years old and you love", hobby)

# 3️⃣ Conditional Statements
age = int(input("Enter your age: "))
if age >= 18:
    print("You're an adult.")
else:
    print("You're a minor.")

# 4️⃣ For Loop
for i in range(1, 6):
    print(i)

# 5️⃣ While Loop
number = int(input("Enter a number (0 to quit): "))
while number != 0:
    print("You entered:", number)
    number = int(input("Enter a number (0 to quit): "))
print("Goodbye!")

# 6️⃣ Functions
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print("Product is:", result)

# ✅ Bonus Challenge
def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")

check_even_odd(10)
check_even_odd(7)
