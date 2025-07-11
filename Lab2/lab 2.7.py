n = int(input("Enter number of points: "))
points = []

for _ in range(n):
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    points.append((x, y))

x0, y0 = points[0]
x1, y1 = points[1]
is_straight = True

for i in range(2, len(points)):
    xi, yi = points[i]
    if (y1 - y0) * (xi - x0) != (yi - y0) * (x1 - x0):
        is_straight = False
        break

if is_straight:
    print("Points form a straight line.")
else:
    print("Points do not form a straight line.")
