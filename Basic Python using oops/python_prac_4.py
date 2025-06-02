# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 09:54:15 2024

@author: Dixit
"""

def fileprocessor(filepath):
    fileobj=open(filepath,'r+')
    x =len( fileobj.read().split(' '))
    y=len( fileobj.read().split('/t'))
    z=len(fileobj.read().split('/n'))
    return (x,y,z)
    fileobj.close()

print(fileprocessor(r"C:\Users\Dixit\Downloads\movie_ratings_dataset.csv"))
