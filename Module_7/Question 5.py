def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Calling the function
result = factorial(5)
print(result)  # Outputs: 120