import matplotlib.pyplot as plt
import numpy as np

def plot_horizontal_stadium(L):
    # Constants
    r = 1

    # Plot shape
    theta = np.linspace(0, np.pi, 100)
    x_circle = r * np.cos(theta)
    y_circle = r * np.sin(theta)
    x_top_line = np.linspace(-r, r, 100)
    y_top_line = np.ones(100) * r
    x_bottom_line = np.linspace(-r, r, 100)
    y_bottom_line = -np.ones(100) * r
    x_left_line = np.linspace(-L/2, L/2, 100)
    y_left_line = np.sqrt(r**2 - (x_left_line**2) / (r**2 / L**2))
    x_right_line = np.linspace(L/2, -L/2, 100)
    y_right_line = np.sqrt(r**2 - (x_right_line**2) / (r**2 / L**2))

    plt.figure(figsize=(8, 8))
    plt.plot(x_circle, y_circle, 'k')
    plt.plot(x_top_line, y_top_line, 'k')
    plt.plot(x_bottom_line, y_bottom_line, 'k')
    plt.plot(x_left_line, y_left_line, 'k')
    plt.plot(x_right_line, y_right_line, 'k')

    # Set plot limits and labels
    plt.xlim(-r - 0.1, r + 0.1)
    plt.ylim(-r - 0.1, r + 0.1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Horizontal Stadium Billiard')

    # Show the plot
    plt.show()

# Set the length of the straight lines (controls the shape of the oval)
L = 0.5

# Plot the horizontal stadium billiard
plot_horizontal_stadium(L)
