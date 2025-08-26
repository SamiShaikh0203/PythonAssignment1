# Program to find area and perimeter of a rectangle

# Input: length and width of the rectangle
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Calculate area
area = length * width

# Calculate perimeter
perimeter = 2 * (length + width)

# Output the results
print(f"Area of the rectangle: {area}")
print(f"Perimeter of the rectangle: {perimeter}")