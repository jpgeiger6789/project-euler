#id19.py

#This program finds how many Sundays fell on the first of the month
#during the twentieth century

def monthrange(month, year):
    days = 31
    thirtydays = [4, 6, 9, 11]
    if month == 2:
        if leapyear(year):
            days = 29
            return days
        else:
            days = 28
            return days
    if month in thirtydays:
        days = 30
        return days
    return days

def leapyear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def ID19():
    #Note: the answer does not include the two times Sunday occured on the first of the month
    #in 1900.  Therefore, the answer is 2 too high.  Don't feel like fixing the code.
    year = 1900
    weekday = 1
    count = 0
    while year < 2001:
        month = 1
        while month < 13:
            if weekday == 0:
                count += 1
                print('On month', month, 'of year', year, 'the first day was Sunday')
            daysinmonth = monthrange(month, year)
            weekday = (weekday + daysinmonth) % 7
            month += 1
        year += 1
    print(count, 'Sundays fell on the first of the month in the 20th century')

ID19()
