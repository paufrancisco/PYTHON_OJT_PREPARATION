class Calculator:
    def add(self, a , b = 0 , c = 0):
        return a + b + c

problem1 = Calculator()


print(problem1.add(5))
print(problem1.add(5,2))
print(problem1.add(5,2,1))