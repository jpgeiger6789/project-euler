#ID21

#This program finds the sum of all amicable numbers under 10,000

def d(x):
    divisors = [1] #adds 1 bc it is a proper divisor but x is not
    for i in range(2, x):
        if i in divisors:
            break
        if x % i == 0:
            divisors.append(i) #previous note was so that this step
            divisors.append(x // i) #can be used to make the algorithm
    dsum = 0                        #more efficient
    for i in divisors:
        dsum += i
    return dsum

def ID21():
    amicablenumbers = []
    for i in range(2, 10000): #1 is not an amicable number
        if i not in amicablenumbers:
            x = d(i)
            if d(x) == i and x != i:
                amicablenumbers.append(i)
                if x < 10000 and x not in amicablenumbers:
                    amicablenumbers.append(x)
    print(amicablenumbers)
    amicablesum = 0
    for i in amicablenumbers:
        amicablesum += i
    print('The sum of all amicable numbers under 10000 is', amicablesum)
    
ID21()
