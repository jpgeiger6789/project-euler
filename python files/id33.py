#id33.py

#this program finds four fractions which, when cancelled incorrectly,
#cancel correctly.
#the answer to problem 33 is the product, simplified, of only such fractions
#which are less than one.  then just the denominator of that product.

def ID33():
    for i in range(1, 10):
        for j in range(1, 10):
            if i != j:
                for k in range(1, 10):
                    if (10 * i + k) / (10 * j + k) == i / j:
                        print('numerator is', i, 'denominator is', j)
                    elif (10 * k + i)/ (10 * j + k) == i / j:
                        print('numerator is', i, 'denominator is', j)
                    elif (10 * i + k) / (10 * k + j) == i / j:
                        print('numberator is', i, 'denominator is', j)
                    elif (10 * k + i) / (10 * k + j) == i / j:
                        print('numerator is', i, 'denominator is', j)

ID33()
