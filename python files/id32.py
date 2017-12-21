#id32.py

#this program finds the sum of all pandigital products

def pandigital(strnums, product):
    listdigits = []
    for i in strnums:
        listdigits.append(i)
    for i in range(1, 10):
        if listdigits.count(str(i)) != 1:
            return 0
    return product

def ID32():
    listproducts = []
    prodsum = 0
    for i in range(1, 1000):
        for j in range(i, 1000):
            product = i * j
            strnums = str(product) + str(i) + str(j)
            strlength = len(strnums)
            if strlength == 9:
                x = pandigital(strnums, product)
                if x not in listproducts:
                    listproducts.append(x)
    for i in range(1000, 10000): #it worked so shut up
        for j in range(1, 100):
            product = i * j
            strnums = str(product) + str(i) + str(j)
            strlength = len(strnums)
            if strlength == 9:
                x = pandigital(strnums, product)
                if x not in listproducts:
                    listproducts.append(x)
    for i in listproducts:
        prodsum += i
    print(listproducts)
    print('The sum of all pandigital products is', prodsum)

ID32()
