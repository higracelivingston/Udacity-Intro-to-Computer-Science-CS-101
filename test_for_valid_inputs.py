def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # Program defensively! Add an assertion if the input is not valid!
    assert dateIsBefore(year1, month1, day1, year2, month2, day2), \
        "The first date must be before the second date."
    
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    test_cases = [((2012, 9, 30, 2012, 10, 30), 30), 
                  ((2012, 1, 1, 2013, 1, 1), 360),
                  ((2012, 9, 1, 2012, 9, 4), 3),
                  ((2013, 1, 1, 1999, 12, 31), "AssertionError")]
    
    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print("Test with data:", args, "failed")
            else:
                print("Test case passed!")
        except AssertionError:
            if answer == "AssertionError":
                print("Nice job! Test case " + str(args) + " correctly raises AssertionError!\n")
            else:
                print("Check your work! Test case " + str(args) + " should not raise AssertionError!\n")

test()
