from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        print ("Wooff")
        
class Cat(Animal):
    def make_sound(self):
        print("Meoww")
        
dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()