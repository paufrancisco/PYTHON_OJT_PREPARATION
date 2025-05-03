class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        return f"This is {cls.__name__} class performing math operations."

# Usage
print(MathOperations.add(5, 7))          # Output: 8
print(MathOperations.description())      # Output: This is MathOperations class performing math operations.
