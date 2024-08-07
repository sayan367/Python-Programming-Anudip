# Function to calculate the fare based on distance
def calculate_fare(distance):
    if distance <= 50:
        fare = distance * 8
    elif distance <= 100:
        fare = (50 * 8) + ((distance - 50) * 10)
    else:
        fare = (50 * 8) + (50 * 10) + ((distance - 100) * 12)
    return fare

# Read the distance from the user
distance = float(input("Enter the distance travelled (in Km): "))

# Calculate the fare
fare = calculate_fare(distance)

# Print the fare
print(f"The fare for {distance} Km is: Rs. {fare:.2f}")
