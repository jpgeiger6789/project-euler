#id41.py

#This program finds the largest n-pandigital prime

from math import sqrt
from random import randrange
from random import randint
from primetest import isprime

flist = []
blist = [9, 8, 7, 6, 5, 4, 3, 2, 1]

tflist = flist
tblist = blist

def ID41(backlist, frontlist):
    backlength = len(backlist)
    frontlength = len(frontlist)
    if backlength == 2:
        backlist[0], backlist[1] = backlist[1], backlist[0]
        numlist = frontlist + backlist
        number = ''
        for i in numlist:
            number += str(i)
        number = int(number)
        if isprime(number):
            print('The number is', number)
            return 1
        backlist[0], backlist[1] = backlist[1], backlist[0]
        return
    else:
        templist = backlist
        for j in templist:
            index = templist.index(j)
            frontlist.append(j)
            backlist.remove(j)
            ID41(backlist, frontlist)
            numlist = frontlist + backlist
            number = ''
            for i in numlist:
                number += str(i)
            number = int(number)
            if isprime(number):
                print('The number is', number)
                return 1
            backlist.insert(index, j)
            frontlist.remove(j)
                    
while True:
    if ID41(blist, flist):
        break
    print('huh')
    flist = tflist
    blist = tblist[1:]
    tblist = blist
