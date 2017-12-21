#id43.py

#This program finds the sum of all pandigital numbers with a given property

#Let d1 be the 1st digit, d2 be the 2nd digit, and so on
#In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17

import itertools

def checknum(num):
    #assume number is in string format
    if int(num[1:4]) % 2:
        return 0
    elif int(num[2:5]) % 3:
        return 0
    elif int(num[3:6]) % 5:
        return 0
    elif int(num[4:7]) % 7:
        return 0
    elif int(num[5:8]) % 11:
        return 0
    elif int(num[6:9]) % 13:
        return 0
    elif int(num[7:]) % 17:
        return 0
    else:
        return int(num)

def ID43():
    '''This function returns the sum of all 10-pandigital numbers with the given
    property.'''
    nlist = []
    for i in range(10):
        nlist.append(str(i))
    perm = itertools.permutations(nlist)
    nsum = 0
    for i in perm:
        if i[0] == 0:
            pass
        else:
            num = ''
            for digit in i:
                num += digit
            nsum += checknum(num)
    return nsum

print(ID43())
