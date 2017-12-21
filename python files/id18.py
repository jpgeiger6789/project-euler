#ID18.py

#this program finds the maximum sum from top to bottom of a triangle.

def ID18():
    file = open('problem18.txt')
    filelist = []
    counter = 2
    for i in file.readlines():
        filelist.append(i[:counter])
        counter += 3
    triangle = []
    for i in filelist:
        triangle.append(i.split())
    counter = 0
    for i in triangle:
        counter2 = 0
        for j in i:
            triangle[counter][counter2] = int(j)
            counter2 += 1
        counter += 1
    length = len(triangle)

    maxsumlist = [[triangle[0][0]]]
    for i in range(1, length):
        linelist = []
        listlength = len(triangle[i])
        for j in range(listlength):
            if j == 0:
                linelist.append(triangle[i][j] + maxsumlist[i - 1][j])
            elif j == listlength - 1:
                linelist.append(triangle[i][j] + maxsumlist[i - 1][j - 1])
            else:
                linelist.append(triangle[i][j] + max(maxsumlist[i - 1][j], maxsumlist[i - 1][j - 1]))
        maxsumlist.append(linelist)
    print('The max is', max(maxsumlist[len(maxsumlist) - 1]))

ID18()
