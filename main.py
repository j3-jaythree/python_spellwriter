import numpy as np
import matplotlib.pyplot as plt

# Points
points = [[0,0], [2.5,-5], [2.5,5], [5,0]]

def draw_arc(x1, x2, y1, y2): 
    # Center
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2

    # Draw points
    plt.plot(x1, y1, color='blue', marker='o')
    plt.plot(x2, y2, color='blue', marker='o')

    # Draw center point
    plt.plot(cx, cy, color='green', marker='o')

    # Radius
    r = np.sqrt(np.power(x1 - cx, 2) + np.power(y1 - cy, 2))
    # avoid divisionby zero
    if x1 == x2:
        start = np.pi/2
    # Asign start
    else:
        start = np.arctan((y2 - cy) / (x2 - cx))
    if x1 < x2 and y1 < y2: #1st cuadrant
        end = start + np.pi # Clockwise
    elif x1 > x2 and y1 < y2: #2nd cuadrant
        end = start - np.pi # Clockwise
    elif x1 < x2 and y1 > y2: #2nd cuadrant
        end = start - np.pi # Clockwise
    else:
        end = start - np.pi # Counterclockwise
    print(start)
    print(end)
    angles = np.linspace(min(start, end), max(start, end), 100)
    xs = r * np.cos(angles) + cx
    ys = r * np.sin(angles) + cy
    plt.plot(xs, ys, color='red')
    
for i in range(0, len(points)-1):
    x1, y1 = points[i]
    x2, y2 = points[i+1]
    draw_arc(x1, x2, y1, y2)
x1, y1 = points[-1]
x2, y2 = points[0]
draw_arc(x1, x2, y1, y2)
plt.xlim([-10,10])
plt.ylim([-10,10])
plt.show()

"""
start = np.arctan((y1-cy)/(x1-cx)+np.pi)
end = np.arctan((y2-cy)/(x2-cx)+np.pi)

print(start)
print(end)

angles = np.linspace(start, end, 100 )
plt.plot(x1, y1, color='blue', marker = 'o')
xs = r * np.cos(angles) + cx
ys = r * np.sin(angles) + cy

print(xs)
plt.plot(xs, ys, color='red')
# Show everything
plt.show()"""
