class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Usage
p1 = Point(1, 2)
p2 = Point(3, 4)
result = p1 + p2
print(result)  # Output: (4, 6)
