#Check whether a number is even or odd using ternary operators

number = int(input("Enter a number: "))# taking input from the user.
result = "Even" if number % 2 == 0 else "Odd" # setting up if statement
print(f"The number is {result}.")# printing the result
