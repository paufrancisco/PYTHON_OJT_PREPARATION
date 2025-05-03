class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

    def __len__(self):
        return len(self.title)

# Usage
book = Book("Python 201")
print(book)         # Output: Book: Python 101
print(len(book))    # Output: 10
