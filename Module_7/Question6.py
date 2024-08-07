import random

# Generate 5 random numbers
numbers = [random.randint(1, 100) for _ in range(5)]

# Find maximum and minimum
max_number = max(numbers)
min_number = min(numbers)

print("Random numbers:", numbers)
print("Maximum number:", max_number)
print("Minimum number:", min_number)
