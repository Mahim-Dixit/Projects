# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:38:19 2024

@author: Dixit
"""

 # Decorator and Closure Practice
 import time

 def Timer(func):
     def wrapper(*args,**kwargs):
         x=time.time()
         func()
         y=time.time()
         print(f"{func.__name__} takes {y-x} seconds")
        
     return wrapper


 @Timer
 def play():
     print("The function plays")
    
 play()

