class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

# Usage
temp = Temperature(0)
print(temp.fahrenheit)  # Output: 32.0

temp.fahrenheit = 212
print(temp._celsius)    # Output: 100.0
