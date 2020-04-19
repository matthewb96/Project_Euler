# -*- coding: utf-8 -*-
"""
    Project Euler Problem 20 - Factorial Digit Sum.
    https://projecteuler.net/problem=20
"""

##### IMPORTS #####
# Standard imports
from math import factorial

# Third party imports


##### FUNCTIONS #####
def sumDigits(num):
    """ Calculates the factorial of `num` then sums the digits. """
    fac = factorial(num)
    digits = [int(i) for i in str(fac)]
    return sum(digits)


##### MAIN #####
if __name__ == '__main__':
    # Seems like too simple a solution but it got in correct
    print(sumDigits(100))
