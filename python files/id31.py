#id31.py

#this program finds the number of ways 2 english pounds can be made from
#smaller units of currency

def waysto200(pounds, english_units):
    unit = english_units[0]
    count = 0

    if pounds + unit == 200:
        count += 1
        if unit > 1:
            count += waysto200(pounds, english_units[1:])
    elif pounds + unit < 200:
        count += waysto200(pounds + unit, english_units)
        if unit > 1:
            count += waysto200(pounds, english_units[1:])
    else:
        count += waysto200(pounds, english_units[1:])
    return count

def ID31():
    english_units = [200, 100, 50, 20, 10, 5, 2, 1]
    count = waysto200(0, english_units)
    print('The number of ways is', count)

ID31()
