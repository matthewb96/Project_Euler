# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 11:48:59 2018

@author: Matthew
Project Euler Problem 5 Smallest multiple
"""

def checkDiv(num):
    """
    Checks that num divides by all number 1 to 20 with no remainder.
    """
    for i in range(20):
        i += 1
        if num % i != 0:
            return False
        
    return True


num = 20
while not checkDiv(num):
    if num % 100000 == 0:
        print("Checked: " + str(num))
    num += 20 #Has to be a multiple of 20 so can just check multiples of 20 to increase speed
    
print("Number is: " + str(num))