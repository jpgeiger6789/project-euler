#id24.py

#This program finds the millionth lexicographic permutation of the digits
#0 through 9

count = [0]
flist = []
blist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def id24(backlist, frontlist, count):
    backlength = len(backlist)
    frontlength = len(frontlist)
    if backlength == 2:
        backlist[0], backlist[1] = backlist[1], backlist[0]
        count[0] += 2
        if count[0] == 1000000:
            print('The permutation is', frontlist + backlist)
            return
        backlist[0], backlist[1] = backlist[1], backlist[0]
        return
    else:
        templist = backlist
        for j in templist:
            index = templist.index(j)
            frontlist.append(j)
            backlist.remove(j)
            id24(backlist, frontlist, count)
            if count[0] == 1000000:
                return
            backlist.insert(index, j)
            frontlist.remove(j)
                    
id24(blist, flist, count)
