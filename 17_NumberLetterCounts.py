# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 18:52:46 2018

@author: Matthew
Project Euler Problem 17 Number letter counts
"""

numLetters = {0:"",
              1:"one",
              2:"two",
              3:"three",
              4:"four",
              5:"five",
              6:"six",
              7:"seven",
              8:"eight",
              9:"nine",
              10:"ten",
              11:"eleven",
              12:"twelve",
              13:"thirteen",
              14:"fourteen",
              15:"fifteen",
              16:"sixteen",
              17:"seventeen",
              18:"eighteen",
              19:"nineteen",
              20:"twenty",
              30:"thirty",
              40:"forty",
              50:"fifty",
              60:"sixty",
              70:"seventy",
              80:"eighty",
              90:"ninety"}

def writeNum(num):
    """
    Finds the string for the number given.
    """
    strNum = str(num)
    digits = len(strNum)
    if digits == 1:
        stringNum = numLetters[num]
    elif digits == 2:
        if num < 20:
            stringNum = numLetters[num]
        else:
            stringNum = numLetters[int(strNum[0]) * 10] + " " + numLetters[int(strNum[1])]
    elif digits == 3:
        stringNum = numLetters[int(strNum[0])] + " hundred"
        if int(strNum[1:]) < 20 and int(strNum[1:]) > 10:
            stringNum += " and " + numLetters[int(strNum[1:])]
        elif strNum[1:] != "00":
            stringNum += " and " + numLetters[int(strNum[1]) * 10] + " " + numLetters[int(strNum[2])]
    elif digits == 4:
        stringNum = numLetters[int(strNum[0])] + " thousand "
    return stringNum

counting = 0
for i in range(1, 1001):
    num = writeNum(i).replace(" ", "")
    print(num)
    counting += len(num)
    
print("Total sum is ", counting)
    
    
    
    
    
    
    
    
    
    
    
    