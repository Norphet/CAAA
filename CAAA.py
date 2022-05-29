from Functions.matrix_generator import matrix_generator_obstacles, matrix_generator, indexmatrix
from Functions.hamilton import hamilton
from Functions.graph_converter import validneighbours

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

# Main Algorithm
print('The requested gaming space:\n',matrix)

# Creating an index matrix for the hamilton path
index_matrix=indexmatrix(matrix)
print('Indexing matrix for the node identification: \n',index_matrix)

# Convert our matrix and index matrix into a graph + set form for the hamilton algorithm
graf=validneighbours(index_matrix, matrix, cell_type)
print('Converted graph logic, showcasing every avaliable route from every cell:\n',graf) 
  
# Hamilton path calculating a manufacturable cell configuration                           
path = hamilton(graf, index_matrix[1][1])
print('Our solution:\n',path)
