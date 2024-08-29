tuples_list = [(1, 2), (3, 4), (5, 6)]

total_sum = sum(sum(tup) for tup in tuples_list)
print(total_sum)  # Output: 21