# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 21:56:31 2018

@author: Matthew
Project Euler Problem 19 Counting Sundays
"""

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

currentYear = 1901
currentMonth = "Jan"
currentDay = 1