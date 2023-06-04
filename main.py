import numpy as np
import matplotlib.pyplot as plt
from utils.utils import create_polygon
from utils.utils import draw_arc

if __name__ == "__main__":
    # Points, Round to avoid errors
    points = np.round(create_polygon(sides=8, length=10), decimals=3)
    print(points)
    # Global center

    # This causes issues with imprecission, for now with regular
    # polygons it will always be 0,0 the center.
    center = [0, 0]
    print(center)

    # Testing purposes
    for i in range(0, len(points)-1):
        x, y = points[i]
        plt.plot(x, y, color='blue', marker='o')
        # plt.annotate(str(i), (x, y), textcoords='offset points', xytext=(0, 10))
    # plt.show()

    # No need to order the points, they are just how I like them

    for i in range(0, len(points)-2):
        for j in range(i+1, len(points)-1):
            x1, y1 = points[i]
            x2, y2 = points[j]
            draw_arc(center, x1, x2, y1, y2)
    # Last with everything
    for i in range(0, len(points)-1):
        x1, y1 = points[-1]
        x2, y2 = points[i]
        draw_arc(center, x1, x2, y1, y2)
    plt.gca().set_aspect('equal')
    plt.axis('off')
    plt.savefig('test.png', bbox_inches='tight', dpi=300)
    plt.show()
