import numpy as np
import matplotlib.pyplot as plt
import utils
# Points
points = np.round(utils.create_polygon(sides=8, length=10), decimals=3)    # Round to avoid errors
print(points)
# Global center

# This causes issues with imprecission, for now with regular
# polygons it will always be 0,0 the center.
# top = np.max(points, axis=0)[1]
# bottom = np.min(points, axis=0)[0]
# left = np.min(points, axis=0)[0]
# right = np.max(points, axis=0)[0]
# center = np.round([(left + right) / 2, (top + bottom) / 2], decimals=3)
center = [0, 0]
print(center)
# plt.plot(center[0], center[1], color='purple', marker='o')


def draw_arc(x1, x2, y1, y2):
    # Center between points
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    print(cx)
    print(cy)
    # Draw points
    plt.plot(x1, y1, color='blue', marker='o')
    plt.plot(x2, y2, color='blue', marker='o')

    # Draw center point
    plt.plot(cx, cy, color='green', marker='o')

    # Radius
    r = np.round(np.sqrt(np.power(x1 - cx, 2) + np.power(y1 - cy, 2)), decimals=3)
    # avoid division by zero
    if x1 == x2:
        start = np.round(np.pi/2, decimals=3)
    # Set start
    else:
        start = np.round(np.arctan((y2 - cy) / (x2 - cx)), decimals=3)
    # Set ends
    if cy == center[1] and cx < center[0]:         # Same distance to axis, idc direction
        end = start - np.pi     # Clockwise
    elif cy == center[1] and cx >= center[0]:
        end = start + np.pi
    elif cy > center[1]:        # Top part
        end = start - np.pi     # Counterclockwise
    elif cy < center[1]:        # Bottom part
        end = start + np.pi     # Clockwise
    else:                       # Shouldn't happen
        end = start             # Cry
        print('cry')
        print(cy)
        print(cx)
        end = np.round(end, decimals=3)
    angles = np.linspace(min(start, end), max(start, end), 100)
    xs = r * np.cos(angles) + cx
    ys = r * np.sin(angles) + cy
    plt.plot(xs, ys, color='red')


for i in range(0, len(points)-2):
    for j in range(i+1, len(points)-1):
        x1, y1 = points[i]
        x2, y2 = points[j]
        draw_arc(x1, x2, y1, y2)
        print(str(i)+"-"+str(j))
# Last with everything
for i in range (0, len(points)-1):
    x1, y1 = points[-1]
    x2, y2 = points[i]
    draw_arc(x1, x2, y1, y2)
    print(str(len(points)-1)+"-"+str(i))
plt.gca().set_aspect('equal')
plt.axis('off')
plt.savefig('test.png', bbox_inches='tight', dpi=300)
plt.show()
