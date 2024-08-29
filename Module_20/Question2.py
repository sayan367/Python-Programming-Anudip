dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate the dictionaries using the `{**dict1, **dict2, **dict3}` syntax
new_dict = {**dic1, **dic2, **dic3}

print("Concatenated Dictionary:", new_dict)