#id38.py

#this program finds the largest pandigital number that can be formed by
#the concantinating the products of x * (1, 2, ... n > 1)

def pandigital(n):
    string = str(n)
    for i in range(1, 10):
        if str(i) not in string:
            return False
    return True

def getprod(n):
    string = ""
    i = 1
    length = 0
    while length < 9:
        string += str(i * n)
        i += 1
        length = len(string)
    if len(string) != 9:
        return 0
    else:
        return int(string)

def ID38():
    maxnum = 0
    for i in range(1, 10000):
        n = getprod(i)
        if n > maxnum:
            if pandigital(n):
                maxnum = n
    print(maxnum)

ID38()
        
