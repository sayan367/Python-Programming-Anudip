# Given string
string = "Welcome to python Training"

# Convert the string to lowercase to make counting case-insensitive
string = string.lower()

# Define a list of vowels
vowels = "aeiou"

# Initialize a counter for vowels
vowel_count = 0

# Initialize a list to store the vowels found in the string
vowels_found = []

# Iterate over each character in the string
for char in string:
    if char in vowels:
        vowel_count += 1
        vowels_found.append(char)

# Print the total count of vowels and the vowels found
print("Total Vowels:", vowel_count)
print("Vowels found:", vowels_found)
