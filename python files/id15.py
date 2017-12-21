#id15.py
#This program finds the number of paths from top-left to bottom-right
#in a 20x20 grid

def numpath(gridsize):
    size = 2
    if gridsize == 1:
        return size
    else:
        for i in range(1, gridsize + 1):
            size = size + numpath(gridsize - 1)
    return size
