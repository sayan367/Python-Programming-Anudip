# Get user input
number = int(input("Enter an integer: "))

# Initialize variables
reversed_number = 0
original_number = number

# Reverse the number using a while loop
while number > 0:
    digit = number % 10
    reversed_number = (reversed_number * 10) + digit
    number //= 10

# Display the result
print(f"The reversed number of {original_number} is {reversed_number}.")
