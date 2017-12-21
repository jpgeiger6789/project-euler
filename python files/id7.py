#ID7

#This program finds the nth prime

def prime(n):
    for i in range(2, int(n ** .5)+ 1):
        if n % i == 0:
            return False
    return True

def ID6():
    n = int(input('Which prime would you like to find? '))
    a = 5
    b = 13
    while a < n:
        if prime(b):
            a += 1
        b += 1
    
    print('Prime', n, 'is', b - 1)

ID6()
