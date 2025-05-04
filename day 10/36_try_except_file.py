# Handling errors during file operations

try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("sample.txt file not found. Please make sure it exists.")
