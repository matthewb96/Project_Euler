# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 12:05:31 2018

@author: Matthew
Project Euler Problem 6 Sum square difference
"""

import numpy as np

values = np.arange(1, 101)
sumValuesSquared = values.sum()**2
squareValues = np.square(values)
sumOfSquares = squareValues.sum()
diff = sumValuesSquared - sumOfSquares

print("Sum Squared = " + str(sumValuesSquared) + ", Sum of Squares = " + str(sumOfSquares) + "\nDifference = " + str(diff))