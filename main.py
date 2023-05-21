import numpy as np
import matplotlib.pyplot as plt

# Points
points = [[0, 0], [2.5, -5], [2.5, 5], [5, 0]]

# Global center

center = np.mean(points, axis=0)
plt.plot(center[0], center[1], color='purple', marker='o')


def draw_arc(x1, x2, y1, y2):
    # Center between points
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2

    # Draw points
    plt.plot(x1, y1, color='blue', marker='o')
    plt.plot(x2, y2, color='blue', marker='o')

    # Draw center point
    plt.plot(cx, cy, color='green', marker='o')

    # Radius
    r = np.sqrt(np.power(x1 - cx, 2) + np.power(y1 - cy, 2))
    # avoid division by zero
    if x1 == x2:
        start = np.pi/2
    # Set start
    else:
        start = np.arctan((y2 - cy) / (x2 - cx))
    # Set ends
    if cx == center[0] or cy == center[1]:  # Same distance to axis, idc if
                                            # it's clock or counterclock
        end = start + np.pi     # Clockwise
    elif cy > center[1]:        # Top part
        end = start - np.pi     # Counterclockwise
    elif cy < center[1]:        # Bottom part
        end = start + np.pi     # Clockwise
    else:                       # Shouldn't happen
        end = start             # Cry
    print(start)
    print(end)
    angles = np.linspace(min(start, end), max(start, end), 100)
    xs = r * np.cos(angles) + cx
    ys = r * np.sin(angles) + cy
    plt.plot(xs, ys, color='red')


for i in range(0, len(points)-2):
    for j in range(i+1, len(points)-1):
        x1, y1 = points[i]
        x2, y2 = points[j]
        draw_arc(x1, x2, y1, y2)
# Last with everything
for i in range (0, len(points)-1):
    x1, y1 = points[-1]
    x2, y2 = points[i]
    draw_arc(x1, x2, y1, y2)
# plt.xlim([-10,10])
# plt.ylim([-10,10])
plt.gca().set_aspect('equal')
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
