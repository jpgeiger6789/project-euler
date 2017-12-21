#ID8

#This program finds the greatest product of five consecutive digits in
#a 1000-digit number

def ID8():
    num = input('What number would you like to check? ')
    maxprod = 0
    for i in range(995):
        a = num[i:i+5]
        b = 1
        for j in a:
            b = b * int(j)
        if b > maxprod:
            maxprod = b
    print(maxprod)
    
ID8()
