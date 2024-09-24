import pandas as pd
from scipy.constants import pi

# Read the CSV file
url = 'https://raw.githubusercontent.com/AnudipAE/DANLC/master/radius_data.csv'
data = pd.read_csv(url)

# Calculate the area of the circle
data['Area'] = pi * (data['Radius'] ** 2)

# Display the first 5 records
print(data.head())

# Save the updated data with areas to a new CSV file
data.to_csv('radius_area_data.csv', index=False)