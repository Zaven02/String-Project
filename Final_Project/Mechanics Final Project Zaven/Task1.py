# I did not manage to make it fully working.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def simulate_billiard(reflection):
    # Initialize variables
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    px = np.random.uniform(-1, 1)
    py = np.random.uniform(-1, 1)
    path = [(x, y)]

    # Simulate reflections
    for _ in range(reflection):
        # Calculate next position
        x += px
        y += py

        # Ensure the path is confined within a unit circle
        norm = np.sqrt(x ** 2 + y ** 2)
        x /= norm
        y /= norm

        # Reflect off the circle
        px = (y ** 2 - x ** 2) * px - 2 * x * y * py
        py = -2 * x * y * px + (x ** 2 - y ** 2) * py

        path.append((x, y))

    return path


# Set the number of reflections and animation interval
reflections = 100
interval = 1000

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
circle = plt.Circle((0, 0), 1, fill=False, color='black')
ax.add_patch(circle)

# Initialize the ball as a point
ball, = ax.plot([], [], 'bo')


def init():
    ball.set_data([], [])
    return ball,


def update(frame):
    path = simulate_billiard(frame)
    x_vals, y_vals = zip(*path)
    ball.set_data(x_vals, y_vals)
    return ball,


# Calculate the total number of frames for the animation
total_frames = reflections + 1

# Animate the ball
animation = FuncAnimation(fig, update, frames=total_frames, init_func=init, blit=True, repeat=False, interval=interval)

# Show the animation
plt.xlabel('x')
plt.ylabel('y')
plt.title('Horizontal Circular Billiard Animation')
plt.grid(True)
plt.show()