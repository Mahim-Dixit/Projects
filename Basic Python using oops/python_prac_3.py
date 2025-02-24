# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 08:45:25 2024

@author: Dixit
"""
class fileop():
    def __init__(self):
        self.fileobj=None
        
    def reader(self,filepath):
        self.fileobj=open(filepath,'r')
        x = self.fileobj.readlines()
         
        self.fileobj.close()
        return x
    def writer(self,filepath,write):
        self.fileobj=open(filepath,'w')
        self.fileobj.writelines(write)
        self.fileobj.close()
    def  read_csv(self,filepath):
        self.fileobj=open(filepath,'r')
        x=self.fileobj.read().split(sep=',')
        return x
        self.fileobj.close()
    def  write_csv(self,filepath,write):
        self.fileobj=open(filepath,'w')
        self.fileobj.writelines(write)
        print("written")
    
        self.fileobj.close()
        
        


if __name__ =='__main__':
        