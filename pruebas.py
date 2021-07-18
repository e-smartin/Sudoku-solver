import numpy as np

def getMatrix(i,j):
    rmin = i // 3 * 3
    cmin = j // 3 * 3 
    rmax = rmin + 3
    cmax = cmin + 3
    print(rmin, cmin)

getMatrix(11,12)
