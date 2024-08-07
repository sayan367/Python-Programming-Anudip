# Function to calculate the net amount after discount
def calculate_net_amount(product_code, order_amount):
    if product_code == 1:  # Battery Based Toys
        if order_amount > 1000:
            discount = order_amount * 0.10
        else:
            discount = 0
    elif product_code == 2:  # Key-based Toys
        if order_amount > 100:
            discount = order_amount * 0.05
        else:
            discount = 0
    elif product_code == 3:  # Electrical Charging Based Toys
        if order_amount > 500:
            discount = order_amount * 0.10
        else:
            discount = 0
    else:
        print("Invalid product code")
        return None
    
    net_amount = order_amount - discount
    return net_amount

# Read product code and order amount from user
product_code = int(input("Enter the product code (1 for Battery Based Toys, 2 for Key-based Toys, 3 for Electrical Charging Based Toys): "))
order_amount = float(input("Enter the order amount: "))

# Calculate the net amount
net_amount = calculate_net_amount(product_code, order_amount)

# Print the net amount
if net_amount is not None:
    print(f"The net amount to be paid is: Rs. {net_amount:.2f}")
