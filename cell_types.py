# This file will contain the cell types, constraints and other important informations 
import numpy as np  

class cell_type():
    def __init__(self):
        self.list_ofconstraints = []

    def additem(x,y,z):
        temp_array = np.array([x,y,z])
        self.list_ofconstraints.append(temp_array )

    def getitem(n):
        return self.list_ofconstraints(n)

Rhombus = cell_type
