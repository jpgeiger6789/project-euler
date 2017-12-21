#ID3.py

#This program finds the largest prime factor of a composite number
#This program works best for numbers 8 or less digits long

#because I keep looking here for this function

from math import sqrt

def prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(3, int(sqrt(n))+ 1, 2):
        if n % i == 0:
            return False
    return True

def ID3(num):
    prime = num
    x = num
    for i in range(2, int(num ** .5)):
        while x % i == 0:
            x = x // i
            prime = i
        if x == 0:
            break
    return prime
