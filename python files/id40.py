#id40.py

#This program finds a given product of digits from the irrational decimal
#produced by concantinating the integers

def getdecimal(nthplace):
    string = ""
    length = len(string)
    i = 0
    while length < nthplace:
        i += 1
        string = string + str(i)
        length = len(string)
    return string

def ID40():
    string = getdecimal(1000000)    
    a = int(string[0])
    b = int(string[9])
    c = int(string[99])
    d = int(string[999])
    e = int(string[9999])
    f = int(string[99999])
    g = int(string[999999])
    ans = a * b * c * d * e * f * g
    print(ans)

ID40()
