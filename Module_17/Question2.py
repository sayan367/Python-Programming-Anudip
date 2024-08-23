try:
    user_input = input("Enter an integer: ")
    user_integer = int(user_input)
    print(f"You entered the integer: {user_integer}")
except ValueError:
    print("Error: The input is not a valid integer!")
