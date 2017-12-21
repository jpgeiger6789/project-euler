#id17.py

#This program sums the number of letters in the numbers, written out, from
#one to one thousand.

def getletters(number):
    wordlist1 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    wordlist2 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    wordlist3 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if number < 10:
        word = wordlist1[number]
        return word
    elif number < 20:
        word = wordlist2[number - 10]
        return word
    elif number < 100:
        num1 = int(str(number)[0])
        num2 = int(str(number)[1])
        word = wordlist3[num1 - 2] + wordlist1[num2]
        return word
    elif number == 1000:
        word = 'onethousand'
        return word
    else:
        num1 = int(str(number)[0])
        num2 = int(str(number)[1])
        num3 = int(str(number)[2])
        if num2 == 0 and num3 == 0:
            word = wordlist1[num1] + 'hundred'
            return word
        else:
            if num2 == 0:
                word = wordlist1[num1] + 'hundredand' + wordlist1[num3]
                return word
            if num2 == 1:
                word = wordlist1[num1] + 'hundredand' + wordlist2[num3]
                return word
            else:
                word = wordlist1[num1] + 'hundredand' + wordlist3[num2 - 2] + wordlist1[num3]
                return word

def ID17():
    word = ''
    for i in range(1, 1001):
        word = word + getletters(i)
    print('The number of letters in the words spelled out from 1 to 1000 is', len(word))

ID17()
