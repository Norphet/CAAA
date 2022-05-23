import numpy as np  

def grid_generator(size):
# grid generation with obsatcels, advanced feature
# basic_grid_cost = np.random.randint(1,2,(n,n))

# Basic grid generation with default cost value 1
    basic_grid_cost= np.ones((size,size))

# obstacle generation at borders.
    for i in range(size):
        for j in range(size):
            if  i==(size-1):
                basic_grid_cost[i][j]=np.random.randint(0,2)
            elif j==0 or j==(size-1):
                basic_grid_cost[i][j]=np.random.randint(0,2)
# manual correction for starting position, for manufacturing reassons
    basic_grid_cost[0][0] = 1
    basic_grid_cost[0][size-1] = 1

    return basic_grid_cost
# the array will be having n elements. TESTING
# print(basic_grid_cost)

