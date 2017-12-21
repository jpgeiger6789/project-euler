#id36.py

#This program finds the sum of all numbers less than one million which are
#palindromic in base 10 and base 2

def palindrome(num):
    strnum = str(num)
    for i in range(len(strnum) // 2):
        if strnum[i] != strnum[-(i + 1)]:
            return False
    return True

def ID36(maxnum):
    count = 0
    for i in range(1, maxnum):
        if palindrome(i) and palindrome(str(bin(i))[2:]):
            count += i

    print('The sum of all numbers which are palindromic in base 10')
    print('and base 2 less than', maxnum, 'is', count)

ID36(1000000)
