# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 15:11:51 2018

@author: Matthew
Project Euler Problem 9 Special Pythagorean triplet
"""

from math import sqrt


def checkTriplet(a, b):
    """
    Check a and b can form a pythagorean triplet, where a < b.
    """
    c = sqrt(a**2 + b**2)
    if c <= b or c != int(c):
        #Not a pythagorean triplet
        return False, None
    else:
        print("Triplet: ({}, {}, {})".format(str(a), str(b), str(c)))
        return True, int(c)

found = False
find = 1000

for a in range(find):
    if found:
        break
    for b in range(a + 1, find + 1):
        check , c = checkTriplet(a, b)
        if check == False:
            continue
        if (a + b + c) == find:
            found = True
            print("a = " + str(a) + ", b = " + str(b) + ", c = " + str(c) + "\nSum = " + str(a+b+c) + "\nProduct = " + str(a*b*c))
            break
        
if found == False:
    print("Couldn't find it.")