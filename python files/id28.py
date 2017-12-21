from numpy import *

def update(matrix, direction, row, column, num):
    '''This function moves one step forward in the matrix (which direction is determined by the 'direction' variable)
    then updates the value of the matrix at the new location to the 'num' variable.  'row' and 'column' determine the
    current location, and 'matrix' is the matrix which is being turned into a spiral'''

    def move_down(row = row):
        row[0] += 1
    def move_left(column = column):
        column[0] -= 1
    def move_up(row = row):
        row[0] -= 1
    def move_right(column = column):
        column[0] += 1
    def revalue(matrix = matrix, row = row, column = column, num = num):
        matrix[row[0], column[0]] = num

    #move right, look down.  move down, look left.  move left, look up. move up, look right.
    if direction[0] == 'right':
        look_down = matrix[row[0] + 1][column[0]]
        if look_down == 0:
            direction[0] = 'down'
            move_down()
            revalue()
        else:
            move_right()
            revalue()
    elif direction[0] == 'down':
        look_left = matrix[row[0]][column[0] - 1]
        if look_left == 0:
            direction[0] = 'left'
            move_left()
            revalue()
        else:
            move_down()
            revalue()
    elif direction[0] == 'left':
        look_up = matrix[row[0] - 1][column[0]]
        if look_up == 0:
            direction[0] = 'up'
            move_up()
            revalue()
        else:
            move_left()
            revalue()
    elif direction[0] == 'up':
        look_right = matrix[row[0]][column[0] + 1]
        if look_right == 0:
            direction[0] = 'right'
            move_right()
            revalue()
        else:
            move_up()
            revalue()
            
def ID28(length):
    '''This function makes a spiral of length 'length'.  It does so by using the numpy matrix function.  It relies on
    the function 'update', which steps one step forward through the matrix before updating itself.'''
    matrix = array([0] * (length ** 2))
    matrix.resize((length, length))
    row = [int(length // 2)]
    column = [int(length // 2) + 1]  #start one to the right, b/c everything was initialized to one.
    direction = ['right']
    matrix[row[0], column[0] - 1] = 1
    matrix[row[0], column[0]] = 2
    #Here I initialize first block to two. in the update function, it moves, then updates, so the first block
    #(or, in this case, the second) has to be manually updated.
    #Also, because everything in the matrix is one, the {if matrix[i,j] == 1} statement will always
    #return true for the first block (again, second), so it will go down before updating the first number (really,
    #the third); hence, the range starting at 3.
    
    for num in range(3, length ** 2 + 1):  #making a matrix
        update(matrix, direction, row, column, num)
    #print(matrix)
    sum1 = 0
    sum2 = 0
    for i in range(length):
        sum1 += matrix[i][i]
    for i, j in zip(range(length), range(length - 1, -1, -1)):
        #print(matrix[i][j])
        sum2 += matrix[i][j]
    print(sum1 + sum2 - 1)
     
ID28(1001)
