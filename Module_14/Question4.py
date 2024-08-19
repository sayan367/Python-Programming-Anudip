def count_vowels(input_str):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_str if char in vowels)
    print(f"Total vowels are: {count}")

# Example usage:
input_str = "Welcome to Python Assignment"
count_vowels(input_str)
