# Program to remove items from set1 that are not common to both sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Updating set1 to keep only common elements
set1.intersection_update(set2)

print(set1)
