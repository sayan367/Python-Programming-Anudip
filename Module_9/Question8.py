# Initialize sum
total_sum = 0

# Accept numbers using a while loop
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    # Check for termination condition
    if number == 0:
        break
    
    # Add the number to the total sum
    total_sum += number

# Display the result
print(f"The sum of all entered numbers is {total_sum}.")
