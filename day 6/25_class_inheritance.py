class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound")
        
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")
        
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meow")
        
dog = Dog("Gobing")
dog.speak()


cat = Cat("Ming ming")
cat.speak()