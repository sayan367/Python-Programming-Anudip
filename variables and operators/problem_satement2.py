"""
A shop will give a discount of 10% if the cost of purchased quantity is more
than 1000.Ask user for quantity Suppose, one unit will cost 100.Judge and print
total cost for user.
"""

# Define the cost per unit
unit_cost = 100

# Ask the user for the quantity they want to purchase
quantity = int(input("Enter the quantity of items you want to purchase: "))

# Calculate the total cost without discount
total_cost = quantity * unit_cost

# Check if the total cost exceeds 1000 to apply a discount
if total_cost > 1000:
    discount = 0.10 * total_cost
    total_cost -= discount
    print(f"A discount of 10% has been applied. The total cost after discount is: {total_cost}")
else:
    print(f"The total cost is: {total_cost}")
