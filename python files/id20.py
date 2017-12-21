#ID20.py

#This program sums the digits of the number 100!.

def factorial(n):
    product = 1
    while n > 1:
        product = product * n
        n = n - 1
    return product

def ID20():
    a = factorial(100)
    totsum = 0
    for i in str(a):
        totsum += int(i)
    print(totsum)
    
ID20()
