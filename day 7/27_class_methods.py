class Person:
    population = 0
    
    def __init__(self,name):
        self.name = name
        Person.population +=1
    @classmethod
    def show_population(cls):
        print(f"Total population : {cls.population}")
        
p1 = Person("jake")
p2 = Person("Pau")

Person.show_population()