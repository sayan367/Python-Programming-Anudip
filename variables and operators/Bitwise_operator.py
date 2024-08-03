# Define two numbers
a = 60  # 60 = 0011 1100 in binary
b = 13  # 13 = 0000 1101 in binary

# Bitwise AND
result = a & b  # 12 = 0000 1100
print(f"Bitwise AND: {result}")

# Bitwise OR
result = a | b  # 61 = 0011 1101
print(f"Bitwise OR: {result}")

# Bitwise XOR
result = a ^ b  # 49 = 0011 0001
print(f"Bitwise XOR: {result}")

# Bitwise NOT
result = ~a  # -61 = 1100 0011 (two's complement)
print(f"Bitwise NOT: {result}")

# Bitwise left shift
result = a << 2  # 240 = 1111 0000
print(f"Bitwise left shift: {result}")

# Bitwise right shift
result = a >> 2  # 15 = 0000 1111
print(f"Bitwise right shift: {result}")
