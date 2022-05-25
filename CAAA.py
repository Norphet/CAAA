from matrix_generator import grid_generator_obstacles, grid_generator

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

#User inputs
size=input('Please enter the Y value for the game grid, size(Y,Y)\n')
size=int(size)
matrix_type=input('Do you want obstacles to be generated? Yes or No\n')
if matrix_type=="Yes":
    matrix = grid_generator_obstacles(size)
elif matrix_type=='No':
    matrix = grid_generator(size)
else:
    print("Invalid choice")  
cell_type=input('Please define the type of cell we are working with: \nRhombus\nHexagon\n ')

#Main Algorithm
if cell_type == 'Hexagon':
    print("You chose Hexagon")    
    print(matrix)

    grid = Grid(matrix=matrix)

    start = grid.node(0, 0)
    end = grid.node(size-2,size-2)

    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    path, runs = finder.find_path(start, end, grid)

    print('operations:', runs, 'path length:', len(path))
    print(grid.grid_str(path=path, start=start, end=end))
    print(path)
    
elif cell_type == 'Rhombus':
    print("You chose Rhombus")
    print(matrix)

    grid = Grid(matrix=matrix)

    start = grid.node(1, 1)
    end = grid.node(size-1,size-1)

    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)

    print('operations:', runs, 'path length:', len(path))
    print(grid.grid_str(path=path, start=start, end=end))
    print(path)

else:
    print("Invalid choice")