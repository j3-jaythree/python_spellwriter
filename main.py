import numpy as np
import matplotlib.pyplot as plt
import utils
# Points, Round to avoid errors
points = np.round(utils.create_polygon(sides=8, length=10), decimals=3)
print(points)
# Global center

# This causes issues with imprecission, for now with regular
# polygons it will always be 0,0 the center.
center = [0, 0]
print(center)

# Ordering the list to first point on the top right point
ai = np.argsort(points, axis=0)
print(np.take_along_axis(points, ai, axis=0))
first_y = np.max(points, axis=0)[1]
print(first_y)
cond = points == first_y
first_x = np.extract(cond, points)
print(first_x)
for i in range(0, len(points)-2):
    for j in range(i+1, len(points)-1):
        x1, y1 = points[i]
        x2, y2 = points[j]
        utils.draw_arc(center, x1, x2, y1, y2)
# Last with everything
for i in range(0, len(points)-1):
    x1, y1 = points[-1]
    x2, y2 = points[i]
    utils.draw_arc(center, x1, x2, y1, y2)
plt.gca().set_aspect('equal')
plt.axis('off')
plt.savefig('test.png', bbox_inches='tight', dpi=300)
plt.show()
