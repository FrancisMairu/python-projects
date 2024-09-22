#surface area of a cylinder provided with radius and height
import math

def cylinder_surface_area(radius, height):
    base_area = math.pi * radius * radius
    lateral_area = 2 * math.pi * radius * height
    surface_area = 2 * base_area + lateral_area
    return surface_area
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

area = cylinder_surface_area(radius, height)

print(f"The surface area of the cylinder is: {area:.2f} square units")
