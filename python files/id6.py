#ID6

#This program finds the difference between the sum of the squares and
#the square of the sums

def ID6():
    n = int(input('What number would you like to go to? '))
    a = 0
    b = 0
    for i in range(1, n + 1):
        a = a + i ** 2
        b = b + i
    b = b * b
    difference = b - a
    print('The difference is ', difference)

ID6()
