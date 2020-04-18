# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 13:30:24 2018

@author: Matthew
Project Euler Problem 16 Power digit sum
"""
import numpy as np


power = 1000
total = 2**power
strTotal = str(total)
arrayTotal = np.fromiter(strTotal, int)
sumDigits = np.sum(arrayTotal)
