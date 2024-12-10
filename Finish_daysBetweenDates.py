def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def daysInMonth(year, month):
    if month == 2:
        return 29 if isLeapYear(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert dateIsBefore(year1, month1, day1, year2, month2, day2), \
        "The first date must be before the second date."
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, expected) in test_cases:
        result = daysBetweenDates(*args)
        if result != expected:
            print(f"Test with data {args} failed. Expected {expected}, got {result}.")
        else:
            print(f"Test with data {args} passed.")

test()
