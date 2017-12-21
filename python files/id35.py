#id35.py
#this program finds the number of circular primes below one million

def prime(n):
    for i in range(2, int(n ** .5)+ 1):
        if n % i == 0:
            return False
    return True

def circularprime(n):
    strn = str(n)
    if not prime(n):
        return False
    for i in range(len(strn)):
        strn = strn[1:]+strn[0]
        if not prime(int(strn)):
            return False
    return True

def ID35(maxnumber):
    count = 0
    for i in range(2, maxnumber):
        if circularprime(i):
            count += 1
    print('The number of primes below', maxnumber, 'is', count)

ID35(1000000)
