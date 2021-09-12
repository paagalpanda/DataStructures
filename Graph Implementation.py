# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 11:36:55 2021

@author: Aditi
"""

class Graph:
    def __init__(self):
        self.noOfNodes = 0
        self.adjacentList = {}
        
    def addVertex(self,node):
        self.adjacentList[str(node)] = []
        self.noOfNodes+=1
        return
    
    def addEdge(self,node1,node2):
        self.adjacentList[str(node1)].append(node2)
        self.adjacentList[str(node2)].append(node1)
        return
        
    def showConnections(self):
        for i in self.adjacentList:
            print(i,self.adjacentList[i])
            
myGraph = Graph()
myGraph.addVertex(0)
myGraph.addVertex(1)
myGraph.addVertex(2)
myGraph.addVertex(3)
myGraph.addEdge(0,2)
myGraph.addEdge(1,2)
myGraph.addEdge(3,2)
myGraph.addEdge(1,3)
myGraph.showConnections()
