p1 = (2,2)
p2= (6,10)

x1,y1 = p1
x2, y2 = p2

slope = float((y2-y1)/(x2-x1))

distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print(f"slope: {slope: .2f} distance: {distance: .2f}")

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("python") == len("dragon"))
print(f"operator to check if 'on' is found in both 'python' and 'dragon' : {'on' in 'python'}")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

floor_div = 7 // 3
print(f"{floor_div} is equal to {int(2.7)}, {floor_div == int(2.7)}")