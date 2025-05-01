from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Subclass must implement make_sound
class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Usage
animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()  # Woof! Meow!
