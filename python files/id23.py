#id23.py

#This program finds the sum of all integers which cannot be written
#as the sum of two abundant numbers

def abundant(x):
    dsum = 1
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            dsum += i
    if dsum > x:
        return True
    else:
        return False

def ID23():
    abundantnumbers = []
    abundantsums = {'a'}
    abundantsums.remove('a')
    for i in range(12, 28124):
        if abundant(i):
            abundantnumbers.append(i)
            for j in abundantnumbers:
                x = i + j
                if x > 28124:
                    break
                abundantsums.add(x)
            #print(len(abundantsums), abundantsums[-1])
    notabundant = []
    for i in range(1, 28124):
        if i not in abundantsums:
            #print(i)
            notabundant.append(i)
        else:
            abundantsums.remove(i)
    notsum = 0
    print(abundantnumbers[:50])
    print(notabundant[:100])
    for i in notabundant:
        notsum += i
    print('The sum of integers that cannot be described as a sum of')
    print('Two abundant integers is', notsum)
    
ID23()
