# Matrix to graph converter for Hamilton Path
#  node conversion comes from pre-installed pacakge

from pathfinding.core.grid import Grid

def findNeighbors(grid)

  for ( int r = -1; r <= 1; r++ )
  
    for ( int c = -1; c <= 1; c++ )
    
      try  
        if ( matrix[row+r][col+c] != '#' ) 
          grid[row][col].addEdge(nodes[row+r][col+c]);
       catch (ArrayIndexOutOfBoundsException e) {}
    

