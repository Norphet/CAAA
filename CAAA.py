from matrix_generator import matrix_generator_obstacles, matrix_generator, indexmatrix
from hamilton import hamilton

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

#User inputs
size=input('Please enter the Y value for the game grid, size(Y,Y)\n')
size=int(size)

matrix_type = None 
while matrix_type not in ("Yes", "No"): 
    matrix_type = input('Do you want obstacles to be generated? Yes or No\n') 
    if matrix_type == "Yes": 
            matrix = matrix_generator_obstacles(size)
    elif matrix_type == "No": 
            matrix = matrix_generator(size) 
    else: 
        print("Please enter Yes or No.") 

cell_type = None 
while cell_type not in ("Rhombus", "Hexagon"): 
    cell_type=input('Please define the type of cell we are working with: \nRhombus\nHexagon\n ') 
    if cell_type == "Hexagon": 
            finder = AStarFinder(diagonal_movement=DiagonalMovement.always) 
    elif cell_type == "Rhombus": 
            finder = AStarFinder(diagonal_movement=DiagonalMovement.never) 
    else: 
        print("Please enter Rhombus or Hexagon.") 

#Main Algorithm
print(matrix)

grid = Grid(matrix=matrix)
index_matrix=indexmatrix(matrix)

print(index_matrix)

start = grid.node(1, 1)
end = grid.node(size,size)

graf = {} 

for x in range(grid.width):
#        print("X:"+str(x))                     TEST
        for y in range(grid.height):
#                print("Y:"+str(y))             TEST
                validPath=set()
                
                if matrix[x][y]!=0:                        
                        if matrix[x-1][y]!=0:
                                validPath.add(int(index_matrix[x-1][y]))
                        if matrix[x][y+1]!=0:
                                validPath.add(int(index_matrix[x][y+1]))
                        if matrix[x+1][y]!=0:
                                validPath.add(int(index_matrix[x+1][y]))
                        if matrix[x][y-1]!=0:
                                validPath.add(int(index_matrix[x][y-1]))
                if (len(validPath) != 0):
                        graf[int(index_matrix[x][y])] = validPath

print(graf)  
                             
path = hamilton(graf, 6)

#path, runs = finder.find_path(start, end, grid)

#print('operations:', runs, 'path length:', len(path))
#print(grid.grid_str(path=path, start=start, end=end))
print(path)
