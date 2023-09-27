
# Ask user to enter the shape of the building
shape = input("Enter the shape of the building, 's' for square, 'r' for round, 'ro' for round:")


# Import PI
import math


# Calculate and display the area
if shape == "s":
    lenght_square = float(input("Please enter the lenght of the square:"))
    square_area = lenght_square **2                       # Formulae for square
    print(f"The foundation of the building will cover {square_area}.")

elif shape == "r":
    lenght_rect = float(input("Please enter the lenght of the rectangular:"))
    width_rect = float(input("Please enter the width of the rectangular:"))
    rectangle_area = lenght_rect * width_rect             # Formulae for rectangular
    print(f"the foundation of your building will cover {rectangle_area}.")

else:
    radius_circle = float(input("Please enter the radius of the circle:"))
    circle_area = math.pi * radius_circle**2              # Formulae for circle
    print(f"The foundation of your building will cover {circle_area}.")
