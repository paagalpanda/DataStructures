# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 11:52:23 2021

@author: Aditi
"""


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        
    def enqueue(self,value):
        newNode = Node(value)
        if self.length==0:
            self.first=newNode
            self.last = newNode
            self.length+=1
        else:
            self.last.next = newNode
            self.last = newNode
            self.length+=1
            
    def dequeue(self):
        print("removed =",self.first.value)
        self.first = self.first.next
        self.length-=1
        
    def printQueue(self):
        currentNode = self.first
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next
            
            
myQueue = Queue()
myQueue.enqueue(10)
myQueue.enqueue(16)
myQueue.enqueue(25)

