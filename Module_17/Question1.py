try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
