# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 08:18:40 2024

@author: Dixit
"""

import numpy as np
import collections
class Stack():
    def __init__(self):
        self.__list=[]
    def push(self,obj):
        self.__list.append(obj)
    def pop(self):
        return self.__list.pop()
    def top(self):
        return self.__list[-1]
    def __len__(self):
        return len(self.__list)
    def is_empty(self):
        return len(self.__list)==0

class Queue():
    def __init__(self):
        self.__array=[]
    def enqueue(self,e):
        self.__array.append(e)
    def dequeue(self):
     return   self.__array.pop(0)
    def first(self):
        return self.__array[0]
    def __len__(self):
      return  len(self.__array)
    def is_empty(self):
        return len(self.__array)==0
    
class LinkedList():
    class _Node:
        def __init__(self,data,nxt):
            self.__data=data
            self.__nxt=nxt
        @property    
        def data(self):
            print("Returning data")
            return self.__data
        @data.setter
        def data_set(self,value):
            print("setting_data")
            self.__data=value
        
        @property
        def nxt(self):
            print("Returning nxt location")
            return self.__nxt
        @nxt.setter
        def nxt_set(self,value):
           print("setting_next location")
           self.__nxt=value 
    def __init__(self):
        self._head=None
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def push(self,e):
        print("Pushing element into linked list")
        self._head=self._Node(e,self.head)
        self._size+=1
    def pop(self):
        if self.is_empty()==True:
            print("The list is empty")
        ans=self.head.data
        self.head=self.head.nxt
        self._size-=1
        return ans
    

class DoublyLinkedList():
    class Node :
        def __init__(self,data,prv,nxt):
            
            self.__data=data
            self.__prv=prv
            self.__nxt=nxt
        @property
        def data(self):
            print("reading data")
            return self.__data
        @property
        def prv(self):
           print("reading prv location")
           return self.__prv
        @property
        def nxt(self):
         print("reading nxt location")   
         return self.__nxt
        @data.setter
        def data_setter(self,value):
            print("Setting data")
            self.__data=value
        @nxt.setter
        def nxt_setter(self,value):
            print("Setting nxt location")
            self.__nxt=value
        @prv.setter
        def prv_setter(self,value):
            print("Setting prv Location")
            self.__prv=value
    def __init__(self):
        self._header=self.Node(None, None, None)
        self._trailer=self.Node(None, None, None)
        self._header.nxt=self._trailer
        self._trailer.prv=self.header
        self._size=0
    def __len__(self):
       return self._size
    def is_empty(self):
        return self._size==0
    def insert_between(self,data,predecessor,succesor):
        newest=self.Node(data, predecessor, succesor)
        predecessor.nxt=newest
        succesor.prv=newest
        self._size+=1
        return newest
    def delete_node(self,node):
        predecessor=node.prv
        sucessor=node.nxt
        predecessor.nxt=sucessor
        sucessor.prv=predecessor
        self._size-=1
        element=node.data
        node._prv=node.nxt=node.data=None
        return element


         
                     
                     
                   

















if __name__=="__main__":
  # x=stack()
   #print(x.push([0,1,2]))
   #print(x.pop())
   #print(x.push(1))
   
   #print(x.top())
   #print(len(x))
   #print(x.is_empty()) 
   
   pass   