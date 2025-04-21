# File handling: Writing to a file
with open("myfile.txt", "w") as file:
    file.write("Hello, this is a Python file!\n")

# File handling: Reading from a file
with open("myfile.txt", "r") as file:
    content = file.read()
    print(content)
