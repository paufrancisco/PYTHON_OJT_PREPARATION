# 22_classes_and_objects.py
# This script introduces the concept of classes and objects in Python.

class Dog:
    # Constructor method to initialize attributes
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Instance method
    def bark(self):
        print(f"{self.name} says Woof!")

    # Another method to get the dog's age in dog years
    def age_in_dog_years(self):
        return self.age * 7


# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

# Calling methods on the objects
dog1.bark()  # Output: Buddy says Woof!
print(f"{dog1.name} is {dog1.age_in_dog_years()} dog years old.")  # Output: Buddy is 21 dog years old.

dog2.bark()  # Output: Lucy says Woof!
print(f"{dog2.name} is {dog2.age_in_dog_years()} dog years old.")  # Output: Lucy is 35 dog years old.
