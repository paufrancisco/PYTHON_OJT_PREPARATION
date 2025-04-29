class Father:
    def skills(self):
        print("Gardening, Programming")
        
class Mother:
    def skills(self):
        print("Cooking , Art")
        
class Child(Father , Mother):
    def skills(self):
        print("sports")
        Father.skills(self)
        Mother.skills(self)
        

child = Child()
child.skills()