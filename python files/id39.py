#id39.py

#this program finds the maximum number of integer solutions for right triangles
#with a perimeter less than a specified amount

def numsolutions(perimeter):
    count = 0
    for a in range(1, perimeter // 2):
        b = (perimeter ** 2 - 2 * perimeter * a)/(2 * perimeter - 2 * a)
        if b == int(b):
            count += 1
    return count

def ID39(maxp):
    maxnum = 0
    p = 0
    for i in range(1, maxp + 1):
        num = numsolutions(i)
        if num > maxnum:
            maxnum = num
            p = i

    print('The perimeter with the greatest number of solutions is', p)

ID39(1000)
