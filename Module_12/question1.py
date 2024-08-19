# Given string
string = "To change the overall look of your document. To change the look available in the gallery"

# Convert the string to lowercase to make the counting case-insensitive
string = string.lower()

# Split the string into words
words = string.split()

# Create an empty dictionary to store the word counts
word_count = {}

# Iterate over each word in the list
for word in words:
    # Update the count for each word in the dictionary
    word_count[word] = word_count.get(word, 0) + 1

# Print the word counts
print("Word Count:", word_count)
