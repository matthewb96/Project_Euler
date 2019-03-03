# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:49:24 2018

@author: Matthew
Project Euler Problem 18 Maximum path sum I
"""
"""
The same index or plus 1 will be the two values that can be used in the next row, with rows increasing in size by one each time.
Max number per row is 99, so when trying routes if one route adds up to more than the next route could possibly add up to by the end the that route can be ignored.
First pick highest values at each attempt then slowly go back down the route trying different attempts.
Stupid idea above, instead start at the bottom and work your way up for every item in the row adding the maximum of the two possibly values to the next row making cumulative values.
"""

from copy import deepcopy

data = """
        75
        95 64
        17 47 82
        18 35 87 10
        20 04 82 47 65
        19 01 23 75 03 34
        88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
        41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
        70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
        63 66 04 68 89 53 67 30 73 16 69 87 40 31
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
        """
data = data.strip()
data = data.split("\n")
graph = []

#Create graph
for i in data:
    graph.append(i.split())
#Convert to int
for i in range(len(graph)):
    for j in range(len(graph[i])):
        graph[i][j] = int(graph[i][j])

#Cumulative graph
cumGraph = deepcopy(graph) #Regular copy doesn't copy the objects inside the list just so if they are changed in one list they are changed in the other
cumGraph.reverse()
for i in range(len(cumGraph)):
    if i == len(cumGraph)-1:
        break
    for j in range(len(cumGraph[i + 1])):
        tests = cumGraph[i][j:j+2]
        #print("trying", tests, ":",cumGraph[i + 1][j], "+=", max(tests))
        cumGraph[i + 1][j] += max(tests)
        #print("=", cumGraph[i+1][j])


print("Max path is", cumGraph[-1][0])
#Finding the route can be done simply by following the maximums down from the top to the bottom