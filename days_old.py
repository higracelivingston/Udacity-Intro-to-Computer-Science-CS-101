# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def is_leap_year(year):
    return year % 4 ==0 and (year % 100 != 0 or year % 400 == 0)
    
def days_in_month(year, month):
    daysOfMonths = [ 31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return daysOfMonths[month-1]
    
def days_in_year(year, month, date):
    days = 0 
    for m in range (1, month):
        days += days_in_month(year, m)
    return days + date
    
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    if (year1, month1, day1) == (year2, month2, day2):
        return 0
    total_days = 0
    for y in range (year1, year2):
        total_days += 366 if is_leap_year(y) else 365
    total_days += days_in_year(year2, month2, day2)
    total_days -= days_in_year(year1, month1, day1)
    return total_days
    
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data: ", args, " failed.")
        else: 
            print ("Sucess!")

test()
    
