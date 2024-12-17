import numpy as np
from math import sin, cos, pi, floor
import matplotlib.pyplot as plt

cylinder_height = 36.5
cylinder_radius = 8.5


def ray_generator(n, radius):
    r = np.sqrt(np.random.uniform(0, 1, n)) * radius
    phi = np.random.uniform(0, 2 * pi, n)
    thetas = (np.sin(np.random.uniform(0, 1, n))) ** 2
    return r, phi, np.array(thetas)


def two_d_lines(r, phi, thetas, h):
    x_on_circle, y_on_circle, x_end, y_end = [], [], [], []
    for i in range(len(r)):
        x_on_circle.append(r[i] * cos(phi[i]))
        y_on_circle.append(r[i] * sin(phi[i]))
        d_z = cos(thetas[i])
        t = h / d_z
        x_end.append(x_on_circle[i] - t * sin(thetas[i]) * cos(phi[i]))
        y_end.append(y_on_circle[i] - t * sin(thetas[i]) * sin(phi[i]))
    return x_on_circle, y_on_circle, x_end, y_end


def interaction_check(xs, ys, xe, ye, radius):
    n_int = 0
    for i in range(len(xs)):
        dy = ye[i] - ys[i]
        dx = xe[i] - xs[i]
        if dx == 0: continue
        a = dy / dx
        x_min = min(xs[i], xe[i])
        x_max = max(xs[i], xe[i])
        x = np.linspace(x_min, x_max, 100)
        for k in range(len(x)):
            x_i = x[k]
            y = a * (x_i - xs[i]) + ys[i]
            if x_i ** 2 + y ** 2 <= radius ** 2:
                n_int += 1
                break
    return n_int


def find_effective_area(cylinder_height, cylinder_radius):
    circle_radii = np.linspace(cylinder_radius, 100, 20)
    effective_areas = []
    for circle_radius in circle_radii:
        n_tot = floor(1500 * (circle_radius ** 2 / cylinder_radius ** 2))
        r, phi, thetas = ray_generator(n_tot, circle_radius)
        x_on_circle, y_on_circle, x_end, y_end = two_d_lines(r, phi, thetas, cylinder_height)
        n_intf = interaction_check(x_on_circle, y_on_circle, x_end, y_end, cylinder_radius)

        circle_area = pi * circle_radius ** 2
        effective_area = (n_intf / n_tot) * circle_area
        effective_areas.append(effective_area)
        print(f"Circle radius: {circle_radius}, Total rays: {n_tot}, Hits: {n_intf}, Effective area: {effective_area}")

    return circle_radii, effective_areas


circle_radii, effective_areas = find_effective_area(cylinder_height, cylinder_radius)

plt.plot(circle_radii, effective_areas)
plt.xlabel("Circle Radius")
plt.ylabel("Effective Area")
plt.title("Effective Area vs Top Circle Radius")
plt.show()
