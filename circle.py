import sys
import math

try:
    radius = float(input('Enter radius of the circle: '))
except ValueError:
    print("Invalid Input")
    sys.exit(1)

area_of_circle =  math.pi * (radius ** radius)
circum_of_circle = 2 * math.pi * radius

print(f"The area of the circle: {area_of_circle:.2f} and the circumference: {circum_of_circle: .2f}")