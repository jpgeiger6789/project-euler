#id27.py

#This program finds a quadratic formula that produces the maximum number of
#primes for consecutive values of n

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** .5)+ 1):
        if n % i == 0:
            return False
    return True

def quad(a, b):
    n = 0
    while True:
        if prime(n ** 2 + a * n + b):
            n += 1
        else: return n

def ID27():
    a = -999
    b = -999
    maxa = -999
    maxb = -999
    maxn = 0
    while a < 1000:
        b = -999
        while b < 1000:
            c = quad(a, b)
            if c > maxn:
                maxa = a
                maxb = b
                maxn = c
                print('a is', a, 'b is', b, 'maxn is', maxn)
            b += 1
        a += 1
    print('a and b are', maxa, 'and', maxb)

ID27()
