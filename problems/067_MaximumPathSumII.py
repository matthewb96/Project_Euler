# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:49:24 2018

@author: Matthew
Project Euler Problem 18 Maximum path sum II
"""

from copy import deepcopy
from time import clock

start = clock()
with open("67_triangle.txt", "r") as file:
    data = file.readlines()

#Create graph
graph = []
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
print("Time taken", (clock() - start)*1000, "ms.")
#Finding the route can be done simply by following the maximums down from the top to the bottom