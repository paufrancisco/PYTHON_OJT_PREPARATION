import logging

# Basic config
logging.basicConfig(level=logging.INFO)

def divide(a, b):
    logging.info(f"Dividing {a} by {b}")
    return a / b

print(divide(10, 2))  # Logs and prints 5.0
