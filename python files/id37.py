#id37.py
#this program finds the number of circular primes below one million

def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(3, int(n ** .5)+ 1, 2):
        if n % i == 0:
            return False
    return True

def truncatableprime(n):
    strn = str(n)
    length = len(strn)
    if not prime(n):
        return False
    for i in range(length - 1):
        strn = strn[1:]
        if not prime(int(strn)):
            return False
    strn = str(n)
    for i in range(length - 1):
        strn = strn[:-1]
        if not prime(int(strn)):
            return False
    return True

def ID35():
    count = 0
    primesum = 0
    i = 11
    while count < 11:
        if truncatableprime(i):
            print(i)
            primesum += i
            count += 1
        i += 1
    print('The sum of all truncatable primes is', primesum)

ID35()
