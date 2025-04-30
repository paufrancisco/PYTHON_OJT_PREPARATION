def binary_to_decimal(binary_str):
    decimal = 0
    power = len(binary_str)-1
    
    for digits in binary_str:
        if digits not in ('0','1'):
            return "Invalid binary number"
        decimal += int(digits) * (2 ** power)
        power -=1
        
    return decimal

print(binary_to_decimal(input("Enter binary number: ")))