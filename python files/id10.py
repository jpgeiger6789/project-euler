#ID10

#This program calculates the sum of all primes below two million

def prime(n):
    for i in range(2, int(n ** .5)+ 1):
        if n % i == 0:
            return False
    return True

def ID10():
    n = int(input('What is the cutoff value for this problem? '))
    a = 1
    b = 2
    primesum = 0
    while b < n:
        if prime(b):
            primesum += b
        b += 1

    print('The sum is', primesum)

ID10()
