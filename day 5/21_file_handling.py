# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, Andreaville!\nWelcome to Day 5 of your Python journey.")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# Appending to a file
with open("sample.txt", "a") as file:
    file.write("\nYou're doing great!")

# Reading again to confirm
with open("sample.txt", "r") as file:
    print("Updated File:\n", file.read())
