# -*- coding: utf-8 -*-
"""
    Project Euler Problem 19 Counting Sundays
"""
##### IMPORTS #####

##### FUNCTIONS #####
def isLeap(year):
    """ Checks if the year given is a leap year and returns bool.

    Parameters
    ----------
    year: int
        The year to check.

    Returns
    -------
    : bool
        - True: is a leap year
        - False: is not a leap year
    """
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False

def nextDate(currDate):
    """ Get the date for the start of the next month after `currDate`.

    Parameters
    ----------
    currDate: list of int
        List containing the day, month (int starting at 0) and year of the current
        date to check.

    Returns
    -------
    date: list of int
        List containing the day, month (int starting at 0) and year of the first day of
        the month after `currDate`.
    """
    if currDate[1] < 11:
        return [1, currDate[1] + 1, currDate[2]]
    else:
        return [1, 0, currDate[2] + 1]

def dateGen(start, endYear):
    """ Generate a list of dates moving to the start of the next month each time. 
    
    Parameters
    ----------
    start: list of int
        The starting date in the format day, month (starting at 0) and year.
    endYear: int
        The year to stop generating, not included.
    
    Yields
    ------
    currDate: list of int
        The date of the first day of the next month in the format day, month (starting at 0)
        and year.
    """
    currDate = start
    while currDate[2] < endYear:
        yield currDate
        currDate = nextDate(currDate)

def daysInMonth(month, year):
    """ Get days in the given month.
    
    Parameters
    ----------
    month: int
        The number of the month starting at 0.
    year: int
        The year, used to check if it's a leap year.
    
    Returns
    -------
    days: int
        Number of days in given `month`.
    """
    if isLeap(year) and month == 1:
        return 29
    else:
        return MONTH_DAYS[month]

def calcDays(startDate, endDate):
    """ Calculates the number of days between `startDate` and `endDate`.
    
    Parameters
    ----------
    startDate: list of int
        List with the form day, month (starting at 0) and year.
    endDate: list of int
        Same format as `startDate`.
    
    Returns
    -------
    days: int
        The number of days between the 2 dates.
    """
    if startDate[1:] != endDate[1:]:
        # Get days left in start date month
        days = daysInMonth(startDate[1], startDate[2]) - startDate[0]
        # Add days into end date month
        days += endDate[0]
    else:
        return endDate[0] - startDate[0]

    # Get months between 2 dates not including the start/end months as they're
    # counted above, year needed for calculating days in each month
    months = lambda mon1, mon2, yr: [(i, yr) for i in range(mon1 + 1, mon2)]
    # Check if months need to roll over to next year
    if startDate[2] != endDate[2]:
        # Get the months until the end of starting year then the months
        # into the ending year
        monthLs = [*months(startDate[1], 12, startDate[2]),
                   *[(i, endDate[2]) for i in range(endDate[1])]]
    else:
        monthLs = months(startDate[1], endDate[1], startDate[2])
    # Sum the days in the month list
    monthDays = [daysInMonth(m, y) for m, y in monthLs]
    days += sum(monthDays)

    # Get years between 2 dates not including the start/end years as they'll be counted above
    yearLs = range(startDate[2] + 1, endDate[2])
    yearDays = [366 if isLeap(y) else 365 for y in yearLs]
    days += sum(yearDays)

    return days

def isSunday(prevSun, currDate):
    """ Calculates the number of days since the previous Sunday to see if `currDate` is a Sunday.

    Parameters
    ----------
    prevSun: list of int
        List containing the day, month (int starting at 0) and year, containing
        the last Sunday found.
    currDate: list of int
        List containing the day, month (int starting at 0) and year of the
        current date to check.

    Returns
    -------
    sunday: bool
        - True: `currDate` is a Sunday
        - False: `currDate` is not a Sunday
    """
    days = calcDays(prevSun, currDate)
    if days % 7 == 0:
        return True
    else:
        return False


##### CONSTANTS #####
MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Date stored as day, month (int starting at 0), year
FIRST_SUNDAY = [7, 0, 1900]


##### MAIN #####
if __name__ == '__main__':
    # Current date, starting in 1901
    currDate = [1, 0, 1901]
    lastSunday = FIRST_SUNDAY.copy()
    endYear = 2001

    print(f'Getting the number of Sundays between {currDate} and {endYear}')

    # Loop through each month checking if the first day is a Sunday
    sundays = 0
    for d in dateGen(currDate, endYear):
        if isSunday(lastSunday, d):
            sundays += 1
            lastSunday = d
    
    print(sundays, 'Sundays')
