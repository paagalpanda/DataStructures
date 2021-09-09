# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 09:22:55 2021

@author: Aditi
"""


class Node:
    def Node(self,value):
        self.left = None
        self.right = None
        self.value = value
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        node = Node(value)
        if self.root:
            currentNode = self.root
            while True:
                if value < currentNode.value:
                    if not currentNode.left:
                        currentNode.left = node
                        return
                    currentNode = currentNode.left
                else:
                    if not currentNode.right:
                        currentNode.right = node
                        return
                    currentNode = currentNode.right
                
    def lookup(self,value):
        currentNode = self.root
        while currentNode:
            if currentNode.value == value:
                return currentNode
            else:
                if value<currentNode.value:
                    currentNode = currentNode.left
                else:
                    currentNode = currentNode.right
            
        return False      

    def remove(self,value):
        currentNode = self.root
        parentNode = None
        
            