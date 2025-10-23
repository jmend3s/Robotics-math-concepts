
import matplotlib.pyplot as plt
import numpy as np


def plot_vector(ax, start, v, label, color):
    ax.quiver(start[0], start[1], start[2], v[0], v[1], v[2], color=color)

    offset = 0.015
    label_coordinates = [0, 0, 0]
    for i in range(3):
        label_coordinates[i] = start[i] + v[i] + offset

    ax.text(label_coordinates[0], label_coordinates[1], label_coordinates[2],
            label,
            color=color,
            fontsize=10)

def plot_reference_frame(ax, start, matrix):
    plot_vector(ax, start, matrix[0], 'X', 'red')
    plot_vector(ax, start, matrix[1], 'Y', 'green')
    plot_vector(ax, start, matrix[2], 'Z', 'blue')

def deg2rad(deg):
    return deg * np.pi / 180

def rotate_vector_x(phi, v):
    Ry = np.array([
        [1, 0, 0],
        [0, np.cos(phi), -np.sin(phi)],
        [0, np.sin(phi), np.cos(phi)]
    ])
    return np.dot(Ry, v)

def rotate_vector_y(theta, v):
    Ry = np.array([
        [np.cos(theta), 0, -np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return np.dot(Ry, v)

def rotate_vector_z(psi, v):
    Rz = np.array([
        [np.cos(psi), -np.sin(psi), 0],
        [np.sin(psi), np.cos(psi), 0],
        [0, 0, 1],
    ])
    return np.dot(Rz, v)

def get_rotation_matrix(phi, theta, psi):
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(phi), -np.sin(phi)],
        [0, np.sin(phi), np.cos(phi)]
    ])
    Ry = np.array([
        [np.cos(theta), 0, -np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    Rz = np.array([
        [np.cos(psi), -np.sin(psi), 0],
        [np.sin(psi), np.cos(psi), 0],
        [0, 0, 1],
    ])
    return np.dot(Rz, np.dot(Ry, Rx))

def rotate_frame(phi, theta, psi, frame):
    rotation_matrix = get_rotation_matrix(phi, theta, psi)
    return np.dot(rotation_matrix, frame)

def main():
    ax = plt.axes(projection='3d')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)

    inertial_matrix = np.identity(3)
    inertial_start = np.array([0, 0, 0])

    body_matrix = inertial_matrix * 0.25
    body_start = np.array([0.4, 0.4, 0])

    plot_reference_frame(ax, inertial_start, inertial_matrix)

    body_matrix = rotate_frame(deg2rad(0), deg2rad(0), deg2rad(45), body_matrix)
    plot_reference_frame(ax, body_start, body_matrix)

    plt.show()

if __name__ == '__main__':
    main()