import numpy as np
from math import sin, cos, pi
import matplotlib.pyplot as plt

phi = []
r = []
thetas = []
cylinder_height = 36.5
cylinder_radius = 8.5
circle_radius = cylinder_radius * 5
n_tot = 10


def ray_generator(n, rho, radius):
    for i in range(n):
        u = np.random.uniform(0, 1)
        r.append(np.sqrt(u * (radius ** 2 - rho ** 2) + rho ** 2))
        phi.append(np.random.uniform(0, 2 * pi))
        while True:
            theta = np.random.uniform(0, np.pi / 2)

            u = np.random.uniform(0, 1)

            if u <= sin(theta) ** 2:
                thetas.append(theta)
                break
    return np.array(thetas)


ray_generator(n_tot, cylinder_radius, circle_radius)
x_on_circle = []
y_on_circle = []
x_end = []
y_end = []


def plot_ray_with_cylinder(rho, height):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    theta = np.linspace(0, 2 * np.pi, 100)

    x_cylinder_bottom = rho * np.cos(theta)
    y_cylinder_bottom = rho * np.sin(theta)
    z_cylinder_bottom = np.zeros_like(x_cylinder_bottom)

    x_cylinder_top = rho * np.cos(theta)
    y_cylinder_top = rho * np.sin(theta)
    z_cylinder_top = height * np.ones_like(x_cylinder_top)

    ax.plot(x_cylinder_bottom, y_cylinder_bottom, z_cylinder_bottom, color='b', label='Cylinder Base (Bottom)')
    ax.plot(x_cylinder_top, y_cylinder_top, z_cylinder_top, color='g', label='Cylinder Base (Top)')

    for i in range(len(theta)):
        ax.plot([x_cylinder_bottom[i], x_cylinder_top[i]],
                [y_cylinder_bottom[i], y_cylinder_top[i]],
                [z_cylinder_bottom[i], z_cylinder_top[i]], color='gray', alpha=0.5)

    theta_circle = np.linspace(0, 2 * np.pi, 100)
    x_big_circle = rho * 10 * np.cos(theta_circle)
    y_big_circle = rho * 10 * np.sin(theta_circle)
    z_big_circle = height * np.ones_like(x_big_circle)

    ax.plot(x_big_circle, y_big_circle, z_big_circle, color='orange', label='Top Circle')

    for i in range(len(r)):
        start_r = r[i]
        start_phi = phi[i]
        theta_ray = thetas[i]
        r_top = rho * 10
        x_start = start_r * cos(start_phi)
        y_start = start_r * sin(start_phi)
        z_start = height
        d_z = cos(thetas[i])
        t = z_start / d_z
        ray_length = 20
        x_ray = x_start - t * sin(theta_ray) * cos(start_phi)
        y_ray = y_start - t * sin(theta_ray) * sin(start_phi)
        z_ray = z_start - t * cos(theta_ray)

        ax.plot([x_start, x_ray], [y_start, y_ray], [z_start, z_ray], color='r')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-1.5 * r_top, 1.5 * r_top])
    ax.set_ylim([-1.5 * r_top, 1.5 * r_top])
    ax.set_zlim([0, ray_length + height])

    plt.legend()
    plt.show()


plot_ray_with_cylinder(5, 10)
