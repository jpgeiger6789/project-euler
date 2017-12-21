#id31.py

#this program finds the number of ways 2 english pounds can be made from
#smaller units of currency

def waysto5(pounds, english_units):
    unit = english_units[0]
    count = 0
    
    if pounds + unit == 5:
        print('if', pounds, english_units)
        count += 1
        if unit > 1:
            print('elif2', pounds, english_units[1:])
            count += waysto5(pounds, english_units[1:])
    elif pounds + unit < 5:
        print('elif', pounds, english_units)
        count += waysto5(pounds + unit, english_units)
        if unit > 1:
            print('elif2', pounds, english_units[1:])
            count += waysto5(pounds, english_units[1:])
    else:
        print('else', pounds, english_units[1:])
        count += waysto5(pounds, english_units[1:])
    return count

def ID31():
    english_units = [5, 2, 1]
    count = waysto5(0, english_units)
    print('The number of ways is', count)

ID31()
