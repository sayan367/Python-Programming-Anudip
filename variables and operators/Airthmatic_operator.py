# Write a program for arithmatic operators
'''
1.      Calculate the area of a circle.

2.      Calculate the area of a triangle.

3.      Calculate the area of a rectangle.

4.      Calculate the area of a square.
'''

# Circle calculation
radius = 5  # Radius of the circle
# Area formula: πr^2 (using an approximation for π)
area_circle = 3.141592653589793 * radius ** 2
# printing the area of the circle
print(f"Area of the circle: {area_circle}")

# Triangle calculation
base = 4  # Base of the triangle
height = 3  # Height of the triangle
# Area formula: 1/2 * base * height
area_triangle = 0.5 * base * height
#printing the area of triangle
print(f"Area of the triangle: {area_triangle}")

# Rectangle calculation
length = 6  # Length of the rectangle
width = 2  # Width of the rectangle
# Area formula: length * width
area_rectangle = length * width
#printing the area of rectangle
print(f"Area of the rectangle: {area_rectangle}")

# Square calculation
side = 4  # Side length of the square
# Area formula: side^2
area_square = side ** 2
#printing the area of square
print(f"Area of the square: {area_square}")
