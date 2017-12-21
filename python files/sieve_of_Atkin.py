#sieve of Atkin
#this is an efficient algorithm for generating a list of primes up to a number

from math import sqrt

def sieve(maxnum):
    resultslist = [2, 3, 5]
    sievelist = []
    for i in range(7, maxnum + 1):
        sievelist.append(i)
    for i in range(1, int(sqrt(maxnum)) + 1):
        for j in range(1, int(sqrt(maxnum)) + 1):
            n = 4 * (i ** 2) + j ** 2
            if n <= maxnum and (n % 12 == 1 or n % 12 == 5):
                sievelist[n - 7] = -n
            n = 3 * (i ** 2) + j ** 2
            if n <= maxnum and (n % 12 == 7):
                sievelist[n - 7] = -n
            n = 3 * (i ** 2) - j ** 2
            if (i > j) and (n <= maxnum) and (n % 12 == 11):
                sievelist[n - 7] = -n      
    for i in sievelist:
        if i < 0:
            count = 1
            notprime = i * i
            placeholder = notprime - 7
            resultslist.append(abs(i))
            while placeholder < maxnum - 7:
                sievelist[placeholder] = abs(sievelist[placeholder])
                count += 1
                placeholder = notprime * count - 7
    return resultslist        
