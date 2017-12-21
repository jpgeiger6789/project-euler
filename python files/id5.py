#ID5

#This program finds the smallest number divisible by each number from 1 to 20

def prime(n):
    for i in range(2, int(n ** .5)+ 1):
        if n % i == 0:
            return False
    return True

def get_prime_factors(num):
    n = num
    L1 = [] #list of prime factors
    L2 = [] #list of times each factor occurs in number
    #L1(i) ** L2(i) multiplied together for each i gives num
    for i in range(2, num // 2 + 1):
        if prime(i):
            while n // i == n / i:
                if i in L1:
                    index = L1.index(i)
                    L2[index] += 1
                else:
                    L1.append(i)
                    L2.append(1)
                n = n / i
    if L1 == []:
        return [num], [1]
    return L1, L2

def combine_factors(L11, L12, L21, L22):
    L1 = []
    L2 = []
    for i in L11:
        L1.append(i)
        if i in L21:
            numtimes = max(L12[L11.index(i)], L22[L21.index(i)])
            L2.append(numtimes)
        else:
            L2.append(L12[L11.index(i)])
    for i in L21:
        if i not in L1:
            L1.append(i)
            L2.append(L22[L21.index(i)])
    return L1, L2
            
def ID5():
    L11 = []
    L12 = []
    for i in range(2, 21):
        L21, L22 = get_prime_factors(i)
        L11, L12 = combine_factors(L11, L12, L21, L22)
    x = 1
    for i in range(len(L11)):
        x = x * (L11[i] ** L12[i])
    print('The smallest number divisible by every number from 2 to 20 is', x)
        
ID5()
