#id34.py

#This program finds the sum of all numbers which are equal to the sum of the
#factorial of their digits

from math import factorial

def ID34():
    factsum = 0
    for i in range(3, 2177280):
        fact = 0
        for j in str(i):
            fact += factorial(int(j))
        if fact == i:
            factsum += i
    print('The sum is', factsum)

ID34()
