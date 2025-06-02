# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 23:44:48 2024

@author: Dixit
"""
import math
class calc():
   def __init__(self,x,y):
       self.x=x
       self.y=y
   def add(self):
       z=self.x + self.y
       return z
   def sub(self):
       z=self.x - self.y
       return z
   def mul(self):
      z=self.x * self.y
      return z
   def div(self):
      z=self.x/self.y
      return z
   def exp(self):
      z,k=math.exp(self.x),math.exp(self.y)
      return z,k
   def  modulus(self):
       z = math.hypot(self.x,self.y)
       return z
       
z=calc(10,15)
print(z.add())
print(z.sub())
print(z.mul())
print(z.div())
print(z.modulus())
print(z.exp())
      
      
      
        
