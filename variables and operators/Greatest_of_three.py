# Initializing  three numbers
num1 = 100
num2 = 500
num3 = 700

# Determine the greatest number
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3

# Print the greatest number
print(f"The greatest of the three numbers is: {greatest}")
