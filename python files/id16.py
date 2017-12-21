#ID16.py

#This program sums the digits of the number 2^1000.

def ID16():
    a = 2 ** 1000
    totsum = 0
    for i in str(a):
        totsum += int(i)
    print(totsum)
    
ID16()
