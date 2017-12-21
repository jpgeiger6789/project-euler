#ID11

#This program finds the highest product of four adjacent numbers in a grid

def ID11():
    file = open('problem11.txt')
    grid = []
    for i in file.readlines():
        grid.append(i[:59])
    gridlist = []
    for i in grid:
        gridlist.append(i.split())
    gridsize = len(gridlist)
    maxproduct = 0
    for i in gridlist: #horizontal products
        for j in range(gridsize - 3):
            product = int(i[j]) * int(i[j + 1]) * int(i[j + 2]) * int(i[j + 3])
            if product > maxproduct:
                maxproduct = product
    for i in range(gridsize): #vertical products
        for j in range(gridsize - 3):
            product = int(gridlist[i][j]) * int(gridlist[i][j + 1]) * int(gridlist[i][j + 2]) * int(gridlist[i][j + 3])
            if product > maxproduct:
                maxproduct = product
    for i in range(gridsize - 3): #top-left to bottom-right
        for j in range(gridsize - 3):
            product = int(gridlist[i][j]) * int(gridlist[i + 1][j + 1]) * int(gridlist[i + 2][j + 2]) * int(gridlist[i + 3][j + 3])
            if product > maxproduct:
                maxproduct = product
    for i in range(3, gridsize):
        for j in range(gridsize - 3): #bottom-left to top-right
            product = int(gridlist[i][j]) * int(gridlist[i - 1][j + 1]) * int(gridlist[i - 2][j + 2]) * int(gridlist[i - 3][j + 3])
            if product > maxproduct:
                maxproduct = product
    print('The max product is', maxproduct)
            
ID11()
