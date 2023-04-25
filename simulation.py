import numpy as np
from matplotlib import pyplot as plt
import random

# Display function
def disp(grid):
    fig, ax = plt.subplots()
    fig.colorbar(ax.imshow(grid, cmap="inferno", vmin=0))
    plt.show()

# Generate a random point on a triangle
# Credit: https://stackoverflow.com/questions/47410054/generate-random-locations-within-a-triangular-domain
def point_on_triangle(pt1, pt2, pt3):
    """
    Random point on the triangle with vertices pt1, pt2 and pt3.
    """
    x, y = sorted([random.random(), random.random()])
    s, t, u = x, y - x, 1 - y
    return (int(s * pt1[0] + t * pt2[0] + u * pt3[0]),
            int(s * pt1[1] + t * pt2[1] + u * pt3[1]))

# The Sierpinski Triangle Simulation
def simulate(grid_size=(101,101), num_iterations=100):
    x, y = grid_size
    # Check grid dimensions
    assert x == y
    # Make grid dim odd, to have a well-defined center point
    if x % 2 == 0:
        x += 1
        y += 1
    grid = np.zeros((x, y))

    # Step 1. Pick 3 points on a grid to form an equilateral triangle T.
    pt1, pt2, pt3 = (0, y // 2), (y - 1, 0), (y - 1, y - 1)
    grid[pt1] = 1
    grid[pt2] = 1
    grid[pt3] = 1
    
    # Step 2. Pick a random point within T.
    starting_point = point_on_triangle(pt1, pt2, pt3)
    grid[starting_point] = 1

    # Step 3. We are now at our starting point p.
    initial_points = (pt1, pt2, pt3)
    for _ in range(num_iterations):
        # Step 4. Pick a random point r from the initial 3 points that formed T.
        r = initial_points[random.randint(0,2)]
        # Step 5. Draw a new point in the middle of the line from p to r.
        starting_point = ((starting_point[0] + r[0]) // 2, (starting_point[1] + r[1]) // 2)
        grid[starting_point] = 1
        # Our new point is our new starting point. Repeat from step 3!
    disp(grid)


simulate(grid_size=(512, 512), num_iterations=80)