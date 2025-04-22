# List comprehension
squares = [x ** 2 for x in range(1,6)]
print("Squares:",squares)

cubes = [x ** 3 for x in range(1,6)]
print("Cubes:",cubes)

even = [x for x in range(1,11) if x % 2 == 0]
print("Even numbers",even)

odd = [x for x in range (1,10) if x % 2 !=0]
print("Odd numbers:", odd)