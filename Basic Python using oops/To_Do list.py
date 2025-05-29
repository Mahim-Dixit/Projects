# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 16:08:29 2024

@author: Dixit
"""
class Todolist():
    def __init__(self):
        self.task_list=[]
        self.task_set={}
    def add_task(self,task):
        self.task_list.append(task)
    def remove_task(self,task):
        self.task_list.remove(task)
    def finalize(self):
      self.task_set={self.task_list[i] for i in range(len(self.task_list))}
    def __repr__(self):
        return f"Your todolist({self.task_set})"
        
class task():
    def __init__(self,task):
        self.task=task
              

if __name__=='__main__':
  todo=Todolist()
  run=True
  while run :
    print(f"Hi /n Welcome to Todo list app \n Choice 1 Enter Task \n Choice 2 Remove Task")
    c=int(input("Enter your Choice"))
    if c==1:
        
    
         notask=int(input("Enter the number of task you want to enter : "))
         for i in range(notask):
             itask=input("Enter the task :")
             tas=task(itask)
             todo.add_task(tas.task)
    if c==2: 
        itas=input("Enter task name to be removed")
        tas=task(itas)
        todo.remove_task(tas.task)
        
    if c == 0:
        run=False
        
    todo.finalize()
    
    print(todo)
        
        
