# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:22:15 2018

@author: Matthew
Project Euler Problem 15 Lattice paths

Using recursion function to calculate total number of paths.
"""

calls = 0
memo = {"0 1":1, "1 0":1} #Use dictionary to remember previously calculated values to reduce number of calls to func
def numWays(x, y):
    """
    Takes the coordinates of the position to calculate number of paths to.
    """
    global calls
    calls += 1
    coords = str(x) + " " +  str(y)
    if x == 0 or y == 0:
        memo[coords] = 1
    elif not coords in memo:
        memo[coords] = numWays(x - 1, y) + numWays(x, y - 1)
    
    #print("Intermediate results for numWays( " , x - 1,", ", y, " ) + numWays( " , x,", ", y - 1, " ) = ", answer)
    return memo[coords]


size = 20
numPaths = numWays(size, size)
print("Number of paths = ", numPaths, ", calls of function = ", calls)