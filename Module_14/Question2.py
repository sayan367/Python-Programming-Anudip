def remove_duplicates(input_str):
    result = []
    for char in input_str:
        if char not in result:
            result.append(char)
    return ''.join(result)

# Example usage:
input_str = "String and String Function"
output_str = remove_duplicates(input_str)
print(output_str)
