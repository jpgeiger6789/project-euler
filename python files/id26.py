#id26.py

from decimal import *
getcontext().prec = 3000

def getlength(string):
    '''this function returns the length of the longest repeating
    series of digits in the string'''
    a = ''
    for i in range(1, len(string) // 2 + 1):
        b = string[-i:]
        c = string[-2 * i :-i ]
        d = string[-3  * i : -2 * i]
        if b == c == d:
            a = b
            #print(a)
            break
    return len(a)

def ID26():
    maxn = 1
    num = 0
    for i in range(1, 1000):
        a = str(Decimal(1) / Decimal(i))[2:-1]
        length = getlength(a)
        if length > maxn:
            maxn = length
            num = i
    return num

a = ID26()
print(a)

#a = str(Decimal(1) / Decimal(713))[2:-1]
#print(getlength(a))
