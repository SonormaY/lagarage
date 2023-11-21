import numpy as np
import matplotlib.pyplot as plt

def draw_plot(x_values, y_values):
    plt.figure(figsize=(10, 9))
    plt.scatter(x_values, y_values, color='red', label='Given points')
    x_range = np.linspace(min(x_values), max(x_values), 100)
    y_range = [lagrange_interpolation(x_values, y_values, x) for x in x_range]
    plt.plot(x_range, y_range, label='Lagrange polynomial')
    plt.title('Lagrange interpolation polynomial')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()


def lagrange_interpolation(x, y, target_x):
    n = len(x)
    result = 0.0

    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (target_x - x[j]) / (x[i] - x[j])
        result += term

    return result

x_values = np.array([10, 15, 16, 17, 20])
y_values = np.array([3, 7, 10, 17, 19])
target_point = 18

interpolated_value = lagrange_interpolation(x_values, y_values, target_point)
print(f"Value in point {target_point}: {interpolated_value}")
draw_plot(x_values, y_values)

