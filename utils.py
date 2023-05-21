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
