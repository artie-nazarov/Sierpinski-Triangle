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
def simulate(grid_size=(101,101)):
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
    print(starting_point)
    grid[starting_point] = 1
    disp(grid)

    # # Test. Make sure this actually forms an equialateral triangle
    # from scipy.spatial import distance
    # a = (0, y // 2)
    # b = (100, 0)
    # c = (100, 100)
    # print(distance.euclidean(a, b))
    # print(distance.euclidean(b, c))
    # print(distance.euclidean(a, c))

simulate()