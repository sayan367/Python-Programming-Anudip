def find_duplicates(lst):
    duplicates = []
    seen = set()

    for item in lst:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)

    return duplicates

# Example usage
numbers = [1, 2, 3, 4, 1, 2, 3, 5]
duplicates = find_duplicates(numbers)
print("Duplicate values:", duplicates)
