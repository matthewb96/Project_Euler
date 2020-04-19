# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 17:51:25 2018

@author: Matthew

Project Euler Problem 4 Largest palindrome product
"""

import numpy as np
import time


def checkPalin(num1, num2):
    """
    Check that number given is a palindrome and return a boolean.
    """
    
    answer = str(num1 * num2)
    reverse = answer[::-1]
    if answer == reverse:
        print("Product of " + str(num1) + " and " + str(num2) + " is a palindrome: " + str(answer))
        return int(answer)
    else:
        return None

start = time.clock()
palindromes = np.array([], dtype = int)
#Change this to stop looking at the same two numbers twice
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        palin = checkPalin(i, j)
        if palin != None:
            palindromes = np.append(palindromes, palin)
        
        try:
            #If the numbers are less than the sqrt of the maximum palindrome the product cannot be higher
            if i < np.rint(np.sqrt(palindromes.max())) and j < np.rint(np.sqrt(palindromes.max())):
                break
        except Exception as error:
            pass
        
print("The largest palindrome is " + str(palindromes.max()))
print("Time taken: " + str(time.clock() - start))