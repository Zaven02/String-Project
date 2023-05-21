import numpy as np
import matplotlib.pyplot as plt

def simulate_vertical_circular_billiard(n, x0, y0, px0, py0):
    reflection = []
    positions = [(x0, y0)]
    momenta = [(px0, py0)]
    reversed_positions = [(x0, y0)]

    for _ in range(n):
        x, y = positions[-1]
        px, py = momenta[-1]

        # Calculate next position based on parabolic path and circle intersection
        alpha = np.arctan2(py, px)
        t = np.linspace(-1, 1, 100)
        path_x = x + t * px
        path_y = y + t * py - 0.5 * 10 * t**2

        # Find intersection with unit circle
        r = np.sqrt(path_x**2 + path_y**2)
        intersect_idx = np.where(r <= 1)[0][0]
        next_x, next_y = path_x[intersect_idx], path_y[intersect_idx]
        reflection.append((next_x, next_y))

        # Calculate new momentum after reflection
        p_x = (next_y**2 - next_x**2) * px - 2 * next_x * next_y * py
        p_y = -2 * next_x * py + (next_x**2 - next_y**2) * py
        momenta.append((p_x, p_y))

        # Save positions for reversed path
        reversed_positions.append((next_x, next_y))

    # Reverse the momentum after n reflections
    momenta_reversed = [(-px, -py) for px, py in momenta]

    # Calculate reversed path
    reversed_reflections = []
    for (x, y), (px, py) in zip(reversed_positions, momenta_reversed):
        alpha = np.arctan2(py, px)
        t = np.linspace(-1, 1, 100)
        path_x = x + t * px
        path_y = y + t * py - 0.5 * 10 * t**2

        r = np.sqrt(path_x**2 + path_y**2)
        intersect_idx = np.where(r <= 1)[0][0]
        reversed_reflections.append((path_x[intersect_idx], path_y[intersect_idx]))

    return reflection, reversed_reflections

# Define initial conditions
n_reflections = 10
x0 = np.random.uniform(-1, 1)
y0 = np.random.uniform(-1, 1)
px0 = np.random.uniform(5, 10)
py0 = np.sqrt(px0**2 - 10 * y0)

# Run the simulation
reflections, reversed_reflections = simulate_vertical_circular_billiard(n_reflections, x0, y0, px0, py0)

# Plotting the paths
fig, ax = plt.subplots()
circle = plt.Circle((0, 0), 1, color='black', fill=False)
ax.add_artist(circle)

x_reflections, y_reflections = zip(*reflections)
x_reversed, y_reversed = zip(*reversed_reflections)

ax.plot(x_reflections, y_reflections, 'ro', label='Original Path')
ax.plot(x_reversed, y_reversed, 'bo', label='Reversed Path')

# Set axis limits and labels
ax.set_aspect('equal')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Vertical Circular Billiard')

# Add legend
ax.legend()

# Display the plot
plt.show()

# Check reversibility
delta = 0.01
deviation = None

for i in range(n_reflections):
    if np.abs(reflections[i][0] - reversed_reflections[i][0]) > delta or \
            np.abs(reflections[i][1] - reversed_reflections[i][1]) > delta:
        deviation = i + 1
        break

if deviation is None:
    print("The path is reversible.")
else:
    print(f"The paths deviate after {deviation} reflections.")
