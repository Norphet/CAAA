from matrix_generator import grid_generator

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

grid = grid_generator(10)
print(grid)