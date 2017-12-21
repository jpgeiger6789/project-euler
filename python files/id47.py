#id47.py

from p_factor import factorization

def ID47():
    numbers = [2, 3, 4, 5]
    while True:
        flen = [len(factorization(x)) for x in numbers]
        if flen == [4, 4, 4, 4]:
            return numbers[0]
        else:
            numbers = [i + 1 for i in numbers]

if __name__ == '__main__':
    print(ID47())
