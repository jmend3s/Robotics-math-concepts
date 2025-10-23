
import matplotlib.pyplot as plt

u = [0, 0, 1]
v = [1, 0, 0]
w = [0, 1, 0]
x = [1, 1, 0]
z = [0, 1, 1]
a = [1, 1, 1]

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

start = [0, 0, 0]

ax.quiver(start[0], start[1], start[2], u[0], u[1], u[2])
ax.quiver(start[0], start[1], start[2], v[0], v[1], v[2])
ax.quiver(start[0], start[1], start[2], w[0], w[1], w[2])
ax.quiver(start[0], start[1], start[2], x[0], x[1], x[2])
ax.quiver(start[0], start[1], start[2], z[0], z[1], z[2])
ax.quiver(start[0], start[1], start[2], a[0], a[1], a[2])

plt.show()
