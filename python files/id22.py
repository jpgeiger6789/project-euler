#id22.py

#This function sorts a list of names then assigns a numerical value to each
#name based on the given rules then sums all the numerical values together

def ID22():
    file = open('problem22.txt')
    x = file.readlines()
    y = x[0].split('","')
    namelist = []
    for i in y:
        if '"' in i:
            x = i.split('"')
            for j in x:
                if j != '':
                    namelist.append(j)
        else:
            namelist.append(i)
    namelist.sort()
    totvalue = 0
    pos = 1
    for i in namelist:
        numsum = 0
        for j in i:
            value = ord(j) - 64
            numsum += value
        totvalue += numsum * pos
        pos += 1
    print('The total name value is', totvalue)
        
ID22()


