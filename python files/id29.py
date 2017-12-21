#ID29.py

#This program finds the number of distinct terms in a stupid sequence

def ID29():
    n = int(input('What two numbers would you like to use? '))
    sequence = []
    for i in range(2, n + 1):
        for j in range(2, n + 1):
            a = i ** j
            if a not in sequence:
                sequence.append(a)
    numterms = len(sequence)
    print('The number of terms is', numterms)

ID29()
