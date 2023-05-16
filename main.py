import numpy as np
import matplotlib.pyplot as plt

# Points
x1 = -10
y1 = 15
x2 = 20
y2 = -5

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

print(r)
start = np.arctan((y2 - y1) / (x2 - x1)) + np.pi
end = np.arctan((y1 - cy) / (x1 - cx)) + np.pi
angles = np.linspace(start, end, 100)
xs = -r * np.cos(angles) + cx
ys = -r * np.sin(angles) + cy
plt.plot(xs, ys, color='red')
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
