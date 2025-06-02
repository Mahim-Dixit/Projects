# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 23:52:52 2024

@author: Dixit
"""
import numpy as np
#Algorithms practice

def Binary_search(it,index):
    '''Sort the list
    Before searching'''
    low=0
    high=len(it)-1
    mid=int((low+high)/2)
    while low <= high:
        if it[mid]==it[index]:
            return it[mid]
        if it[mid]>it[index]:
            high=mid-1
        if it[mid]<it[index]:
            low=mid+1
            
            
def Selection_sort(it,index):
    '''first select then sort'''
    def smallest(it):
        low=0
        smallest=it[0]
        for i in range(len(it)):
            if smallest > it[i]:
                low=i
                smallest=it[i]
        return low
    it2=np.array([])
    for item in range(len(it)) :
        x=smallest(it)
        it2.append(it.pop(x))
    t=it.__class__(it2)
    return t

    
                
            