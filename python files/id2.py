#ID2.py

#This program sums the even-valued fibonacci numbers less than 4 million

def ID2():
    num = int(input('What number would you like to go to? '))
    x = 1
    a = 0
    b = 0
    ans = 0
    while x + a <= num:
        b = x
        x += a
        a = b
        if x % 2 == 0:
            ans += x
    print('The answer is ', ans)

ID2()
