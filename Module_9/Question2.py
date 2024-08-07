# The number to guess
correct_number = 7

while True:
    # Get user input
    guess = int(input("Guess the number (1-10): "))
    
    # Check if the guess is correct
    if guess == correct_number:
        print("Congratulations! You guessed the number.")
        break  # Exit the loop
    else:
        print("Wrong guess, try again.")
