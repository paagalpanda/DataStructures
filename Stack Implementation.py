# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 09:55:30 2021

@author: Aditi
"""


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
        
    def push(self,value):
        newNode = Node(value)
        if self.length==0:
            self.top=newNode
            self.bottom = newNode
            self.length+=1
        else:
             newNode.next = self.top
             self.top = newNode
             self.length+=1
             
    def pop(self):
        print("poped=",self.top.value)
        self.top = self.top.next
        self.length-=1
        
    def peek(self):
        return self.top.value
    
    def printStack(self):
        currentNode = self.top
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next
    
    def isEmpty(self):
        if self.length:
            return False
        else:
            return True
        
        
myStack = Stack()
print("Stack is empty =",myStack.isEmpty())
myStack.push(10)
myStack.push(16)
myStack.push(25)
myStack.printStack()
print("top =",myStack.peek())
myStack.pop()
myStack.printStack()
print("top =",myStack.peek())
print("Stack is empty =",myStack.isEmpty())