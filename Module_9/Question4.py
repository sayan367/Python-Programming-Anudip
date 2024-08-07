# Get user input
number = int(input("Enter a positive integer: "))

# Initialize variables
factorial = 1
current = number

# Ensure the number is positive
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate factorial using a while loop
    while current > 0:
        factorial *= current
        current -= 1

    # Display the result
    print(f"The factorial of {number} is {factorial}.")
