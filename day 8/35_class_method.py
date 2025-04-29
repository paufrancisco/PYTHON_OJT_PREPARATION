class Person:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Person.count += 1
        
    @classmethod
    def total_people(cls):
        return cls.count
    
p1 = Person("Alice")
p2 = Person("Bob")
p3 = Person("Bob")
p4 = Person("Bob")
print(f"Total Person: {Person.total_people()}")