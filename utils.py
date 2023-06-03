import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon


# Create regular polygon
def create_polygon(sides=8, length=1):
    #a, plot = plt.subplots(1)
    pol = RegularPolygon((0, 0), numVertices=sides, radius=length)
    verts = pol.get_path().vertices
    trans = pol.get_patch_transform()
    points = trans.transform(verts)
    return points


def draw_arc(center, x1, x2, y1, y2):
    # Center between points
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
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

