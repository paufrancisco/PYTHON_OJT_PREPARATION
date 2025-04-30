def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return '0'
    
    binary_str = ''
    while decimal_num > 0:
        remainder = decimal_num % 2      # Get remainder (0 or 1)
        binary_str = str(remainder) + binary_str  # Append remainder to the front
        decimal_num = decimal_num // 2   # Update decimal number with quotient
    
    return binary_str

# Example usage
decimal_input = int(input("Enter a decimal number: "))
binary_output = decimal_to_binary(decimal_input)
print(f"Binary equivalent: {binary_output}")