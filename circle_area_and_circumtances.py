import math
rad = float(input("Enter the radius value of a circle: "))
area = math.pi * math.pow(rad, 2)
circum = 2 * math.pi * rad
print(f"The area of circle is: {area}")
print(f"The circumference of circle is: {circum}")
