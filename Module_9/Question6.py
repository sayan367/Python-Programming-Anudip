# Get user input
number = int(input("Enter an integer: "))

# Initialize variables
original_number = number
reversed_number = 0

# Reverse the number
while number > 0:
    digit = number % 10
    reversed_number = (reversed_number * 10) + digit
    number //= 10

# Check if the number is a palindrome
if original_number == reversed_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")
