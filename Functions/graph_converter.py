# A converter function that changes our matrix inputs into graph-s and sets for the hamilton algorithm 

def validneighbours(index_matrix, matrix, cell_type):

  graph = {} 

  for x in range(len(matrix)):
  #        print("X:"+str(x))                     TEST
          for y in range(len(matrix[0])):
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
                          if cell_type=="Hexagon":
                                  if matrix[x-1][y-1]!=0:
                                          validPath.add(int(index_matrix[x-1][y-1]))
                                  if matrix[x+1][y+1]!=0:
                                          validPath.add(int(index_matrix[x+1][y+1]))
                                  if matrix[x+1][y-1]!=0:
                                          validPath.add(int(index_matrix[x+1][y-1]))
                                  if matrix[x-1][y+1]!=0:
                                          validPath.add(int(index_matrix[x-1][y+1]))   
                  if (len(validPath) != 0):
                          graph[int(index_matrix[x][y])] = validPath
  return graph