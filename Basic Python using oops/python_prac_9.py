# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 19:41:18 2024

@author: Dixit
"""

class ComplexNumber():
   def __init__(self,real,imaginary):
       self.real=real
       self.imaginary=imaginary
   def __add__(self,com_other):
       a=self.real+com_other.real
       b=self.imaginary+com_other.imaginary
       return ComplexNumber(a, b)
   def __mul__(self,com_other):
       a=self.real*com_other.real-self.imaginary*com_other.imaginary
       b=self.real*com_other.imaginary+self.imaginary*com_other.real
       return ComplexNumber(a, b)
   def __eq__(self,com_other):
       if self.real == com_other.imaginary and self.imaginary==com_other.imaginary:
           return True
       else:
           return False
   def __repr__(self):
       return f"Complex Number ({self.real}+i{self.imaginary})"
if __name__ == "__main__":
     x=ComplexNumber(2, 3)
     y=ComplexNumber(4, 5)
     z=x+y
     print (z)
           