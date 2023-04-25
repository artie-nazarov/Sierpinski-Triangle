import numpy as np
from matplotlib import pyplot as plt

# Display function
def disp(grid):
    fig, ax = plt.subplots()
    fig.colorbar(ax.imshow(grid, cmap="inferno", vmin=0))
    plt.show()

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
    grid[0, y // 2] = 1
    grid[-1, 0] = 1
    grid[-1, -1] = 1
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