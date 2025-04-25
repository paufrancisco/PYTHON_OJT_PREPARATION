class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
        
    def describe(self):
        print(f"This is a car {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla")
car2 = Car("Ford", "Mustang")

car1.describe()
car2.describe()