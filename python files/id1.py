#ID1.py

#this program adds all numbers less than x which are multiples of 3 or 5.

def ID1():
    x = int(input('What range would you like to run this program over? '))
    sum1 = 0
    for i in range(x):
        if i % 3 == 0 or i % 5 == 0:
            sum1 += i
    print('The sum is ', sum1)

ID1()
