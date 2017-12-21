#ID25.py

#This program finds the first fibonacci number with 1000 digits

def ID25():
    numdig = int(input('What is the number of digits? '))
    x = 1
    a = 0
    b = 0
    length = 0
    fibnum = 1
    while length < numdig:
        b = x
        x += a
        a = b
        tlength = len(str(x))
        if tlength > length:
            length = tlength
        fibnum += 1
    print('The number is ', fibnum)

ID25()
