import math
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
def quadrant(x, y):
    if x > 0 and y > 0:
        return "First Quadrant"
    elif x < 0 and y > 0:
        return "Second Quadrant"
    elif x < 0 and y < 0:
        return "Third Quadrant"
    elif x > 0 and y < 0:
        return "Fourth Quadrant"
    elif x == 0 and y == 0:
        return "Origin"
    elif x == 0:
        return "Y-axis"
    else:
        return "X-axis"
print("Point 1 lies in:", quadrant(x1, y1))
print("Point 2 lies in:", quadrant(x2, y2))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance =", round(distance, 2))