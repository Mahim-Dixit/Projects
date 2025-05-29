# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:42:04 2024

@author: Dixit
"""
class library_system():
    def __init__(self):
        self.books=[]
        self.users=[]
        
    def add_book(self,book):
        self.books.append(book)
    def remove_book(self,book):
        self.books.remove(book)
    def search_book(self,book):
        for i in self.books:
            if i.name == book.name:
                return i
            else:
                return f'{book} not found'
    def add_user(self,user):
        self.users.append(user)
    def remove_user(self,user):
        self.users.remove(user)
    def borrow_book(self,book,user):
        self.books.remove(book)
        user.books.append(book)
        return f'{user.id} has the {book.name} by {book.author}'
    def return_book(self,book,user):
        self.books.append(book)
        user.books.remove(book)
        return f'{user.id} has returned the {book.name} by {book.author}'
    def __repr__(self):
        return f'The Library ({len(self.books)} books, {len(self.users)} users) '
    
        

class book():
    def __init__(self,name,author,price):
        self.name=name
        self.author=author
        self.price=price
    
class user():
    def __init__(self,id,):
        self.id=id
        self.books=[]
        
        
if __name__=='__main__':
    bk1=book('semiconductor physics','Donald A Neaman',200)
    lb1=library_system()
    lb1.add_book(bk1)
    us1=user(1)
    lb1.add_user(us1)
    print(lb1)
