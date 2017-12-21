#id30.py

#This program finds the sum of all numbers which can be written
#as the fifth power of their digits

def ID30():
    fifthlist = []
    for i in range(10, 295245):
        tempsum = 0
        for j in str(i):
            tempsum += int(j) ** 5
        if tempsum == i:
            fifthlist.append(i)
    print(fifthlist)

ID30()
