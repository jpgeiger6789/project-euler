#ID14.py

#This program iterates the Collatz sequence (I think) for all numbers under
#1 million and finds which has the longest chain.

def Collatz(num):
    x = num
    sequence = 1
    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        sequence += 1
    return sequence

def ID14():
    num = 0
    sequence = 0
    for i in range(1,1000000+1):
        q = Collatz(i)
        if q > sequence:
            num = i
            sequence = q
    print('The number is', num)
    print('The sequence value is', sequence)

ID14()
        
