#ID13

#This program finds the first ten digits of the sum of 100 50-digit numbers

def ID13():
    file = open('problem13.txt')
    numsum = 0
    for i in file.readlines():
        numsum += int(i)
    print('The answer is', str(numsum)[:10])
            
ID13()
