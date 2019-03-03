# -*- coding: utf-8 -*-
"""
Project Euler Problem 19 Counting Sundays
WIP - Still working on this problem.
"""
##### IMPORTS #####

##### FUNCTIONS #####
def isLeap(year):
    """
    Checks if the year given is a leap year and returns bool.
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

def calcDays(curDate, curMonth, curYear):
    """
	Calculates the number of days since the previous Sunday.
    """
    # Calculate the number of days since the previous Sunday and if that number is divisible by 7 then today is also a Sunday.
    # Change in date since previous Sunday
    dateDiff = curDate - startDate
    # Months passed since previous Sunday
    monthDays = 0
    while curMonth != sunMonth:
        # Need to loop through the months adding up the days as we go
	pass
    # Then need to loop through the years and add them up to
    return

##### MAIN #####
# Number of days per month (regular year)
daysMonth = {
        "Jan":31,
        "Feb":28,
        "Mar":31,
        "Apr":30,
        "May":31,
        "Jun":30,
        "Jul":31,
        "Aug":31,
        "Sep":30,
        "Oct":31,
        "Nov":30,
        "Dec":31
        }
# List of the reverse order of months
months = ['Dec', 'Nov', 'Oct', 'Sep', 'Aug', 'Jul', 'Jun', 'May', 'Apr', 'Mar', 'Feb', 'Jan']

# Variables to keep track of date of previous Sunday starting on first Sunday in 20th century
sunYr = 1900
sunMonth = "Jan"
sunDate = 7

# Current date, starting in Feb 1900 (we know 1st Jan 1900 is Monday)
curYr = 1900
curMonth = "Feb"
curDate = 1
