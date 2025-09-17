import numpy as np

from pathfinding3d.core.diagonal_movement import DiagonalMovement
from pathfinding3d.core.grid import Grid
from pathfinding3d.finder.a_star import AStarFinder
from pathfinding3d.finder.theta_star import ThetaStarFinder

import time

start_time = time.monotonic()

# Create a 3D numpy array with 0s as obstacles and 1s as walkable paths
matrix = np.ones((500, 500, 500), dtype=np.int8)

# Create a grid object from the numpy array
grid = Grid(matrix=matrix)

# Mark the start and end points
start = grid.node(0, 0, 0)
end = grid.node(490, 490, 490)

# Create an instance of the A* finder with diagonal movement allowed
finder = ThetaStarFinder(diagonal_movement=DiagonalMovement.always)
path, runs = finder.find_path(start, end, grid)

# Path will be a list with all the waypoints as nodes
# Convert it to a list of coordinate tuples
path = [p.identifier for p in path]

print("operations:", runs, "path length:", len(path))
print("path:", path)

print(f"time: {time.monotonic() - start_time}")