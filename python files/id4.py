#ID4

#This program finds the largest palindrome from the product of
#two three digit numbers

def getlist():
    list1 = []
    for i in range(111, 999):
        for j in range(i, 999):
            list1.append(i * j)
    return list1

def ID4():
    w = getlist()
    x = ''
    y = []
    z = 0
    for i in w:
        x = str(i)
        z = len(x)
        if z == 5:
            if (x[0] == x[4] and x[1] == x[3]):
                y.append(i)
        else:
            if (x[0] == x[5] and x[1] == x[4] and x[2] == x[3]):
                y.append(i)
    print(max(y))

ID4()
