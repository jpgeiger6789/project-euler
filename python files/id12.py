#ID12

#This program finds the first triangle number with over 500 divisors

def divisors(x):
    divisors = []
    for i in range(1, x + 1):
        if i in divisors:
            break
        if x % i == 0:
            divisors.append(i)
            divisors.append(x // i)
    return len(divisors)

def ID12():
    x = 0
    for i in range(1, (10 ** 999)):
        x += i
        if divisors(x) > 500:
            print('The lowest triangle number is', x)
            return(x)
        
ID12()
