# Program to return elements present in set A or B but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Using symmetric difference to get elements in set1 or set2 but not both
symmetric_diff = set1.symmetric_difference(set2)

print(symmetric_diff)
