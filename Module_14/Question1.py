def count_characters(input_str):
    chars = digits = symbols = 0

    for char in input_str:
        if char.isalpha():
            chars += 1
        elif char.isdigit():
            digits += 1
        else:
            symbols += 1

    print(f"Chars = {chars}, Digits = {digits}, Symbols = {symbols}")

# Example usage:
input_str = "P@#yn26at^&i5ve"
count_characters(input_str)
