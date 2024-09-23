
def product_of_digits(number):
    # Convert the number to a string to iterate through its digits
    num_str = str(number)

    # Initialize the product to 1
    product = 1

    # Iterate through each digit and calculate the product
    for digit in num_str:
        if digit.isdigit():
            product *= int(digit)

    return product

# Initialize an empty list to store numbers
numbers = []

try:
    # Continue reading input until EOFError is raised
    while True:
        user_input = input("Enter a multidigit number (press Ctrl+D or Ctrl+Z to finish): ")
        numbers.append(int(user_input))
except EOFError:
    pass  # Catch EOFError when there's no more input

# Find the number with the maximum product of digits
max_number = max(numbers, key=product_of_digits, default=0)

# Calculate and display the product of digits of the biggest number
result = product_of_digits(max_number)
print("Product of digits of the biggest number:", result)
