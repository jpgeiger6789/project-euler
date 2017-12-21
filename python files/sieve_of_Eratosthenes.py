#sieve of Eratosthenes
#this is an efficient algorithm for finding whether a number is prime

def sieve(maxnum):
    primelist = [2]
    for i in range(3, num + 1, 2):
        primelist.append(i)
    for i in primelist:
        num = i
        while num < maxnum:
            primelist.remove(num)
