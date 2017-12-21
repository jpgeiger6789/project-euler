#ID9

#This program finds the product of the Pythagorean triplet whose sum is 1000

def ID9():
    a = 0
    b = 0
    c = 0
    for i in range(1, 500):
        for j in range(i, 600):
            if int((i ** 2 + j ** 2) ** .5) == (i ** 2 + j ** 2) ** .5:
                a = i
                b = j
                c = int((i ** 2 + j ** 2) ** .5)
                d = a * b * c
                if a + b + c == 1000:
                    print('A is', a, 'b is', b, 'c is', c)
                    print('The product is', d)
                    return 0
ID9()
