def split_list(lst, first_part_length):
    if first_part_length > len(lst):
        return lst, []

    first_part = lst[:first_part_length]
    second_part = lst[first_part_length:]
    return first_part, second_part

# Example usage
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
first_part_length = 3
first_part, second_part = split_list(original_list, first_part_length)
print("Splitted the list into two parts:", (first_part, second_part))
