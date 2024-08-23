def find_largest_and_smallest(lst):
    if not lst:
        return None, None

    largest = smallest = lst[0]

    for item in lst[1:]:
        if item > largest:
            largest = item
        if item < smallest:
            smallest = item

    return largest, smallest

# Example usage
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
largest, smallest = find_largest_and_smallest(numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)
