
import matplotlib.pyplot as plt
import numpy as np


def deg2rad(deg):
    return deg * np.pi / 180

def rotate_z(theta, v):
    Rz = [
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1],
    ]
    return np.dot(Rz, v)

def rotate_y(theta, v):
    Ry = [
        [np.cos(theta), 0, -np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ]
    return np.dot(Ry, v)

def plot_vector(v, ax, label, color):
    start = [0, 0, 0]
    ax.quiver(start[0], start[1], start[2], v[0], v[1], v[2], color=color)
    offset = 0.015
    ax.text(v[0] + offset, v[1] + offset, v[2] + offset,
            label,
            color=color,
            fontsize=10)

def main():
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)

    u = [1, 0, 0]
    plot_vector(u, ax, 'u', 'blue')

    u = rotate_z(deg2rad(45), u)
    plot_vector(u, ax, 'u45degZ', 'red')

    u = rotate_y(deg2rad(-45), u)
    plot_vector(u, ax, 'u45degY', 'green')

    plt.show()

if __name__ == '__main__':
    main()