# This function will generate the base grid network, and assoicated costs, and obstacle tile
import numpy as np  

def indexmatrix(matrix):
    result=np.ones(np.shape(matrix))
    counter=0
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            result[x][y]=counter   
            counter=counter+1
    return result

def matrix_generator_obstacles(size):
    # grid generation with obsatcels, advanced feature
    # basic_grid_cost = np.random.randint(1,2,(n,n))

    # Basic grid generation with default cost value 1
    basic_grid_cost= np.ones((size+2,size+2))

    # obstacle generation at borders.
    for i in range(size+2):
        for j in range(size+2):
            if  i==(size):
                basic_grid_cost[i][j]=np.random.randint(0,2)
            elif j==1 or j==(size):
                basic_grid_cost[i][j]=np.random.randint(0,2)
            elif i==(size+1) or i==(0): 
                basic_grid_cost[i][j]=0   
            elif j==0 or j==(size+1):
                basic_grid_cost[i][j]=0    
    # manual correction for starting position, for manufacturing reassons
    basic_grid_cost[1][1] = 1
    basic_grid_cost[1][size] = 1
    basic_grid_cost[size][size] = 0
    basic_grid_cost[size][1] = 0
    basic_grid_cost[0][1] = 0
    basic_grid_cost[1][0] = 0
    basic_grid_cost[0][size] = 0
    basic_grid_cost[1][size+1] = 0
    basic_grid_cost[size][0] = 0
    basic_grid_cost[size+1][1] = 0
    basic_grid_cost[size][size+1] = 0
    basic_grid_cost[size+1][size] = 0
    return basic_grid_cost

def matrix_generator(size):
    # grid generation with obsatcels, advanced feature
    # basic_grid_cost = np.random.randint(1,2,(n,n))

    # Basic grid generation with default cost value 1
    basic_grid_cost= np.ones((size+2,size+2))

    # obstacle generation at borders.
    for i in range(size+2):
        for j in range(size+2):
            if i==(size+1) or i==(0): 
                basic_grid_cost[i][j]=0   
            elif j==0 or j==(size+1):
                basic_grid_cost[i][j]=0    
    return basic_grid_cost