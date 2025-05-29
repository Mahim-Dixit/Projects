# -*- coding: utf-8 -*-
# Copyright (c) 2025 Mahim Dixit
# All rights reserved.
# Unauthorized use, modification, or distribution of this software is strictly prohibited.


class bank():
    def __init__(self):
       self.accounts=[]
    def add_account(self,account):
        self.accounts.append(account)
    def remove_account(self,account):
        self.accounts.remove(account)
    def get_info(self,account):
        print(account)
    def __repr__(self):
        return f'Bank(Account_no={len(self.accounts)}'
    

class account():
    def __init__(self,amount,account_id):
        self.amount=amount
        self.account_id=account_id
    def withdraw(self,amount):
        z=self.amount-amount
        if z <0 : print("you dont have enough money in your bank account")
        else : self.amount=z
    def deposit (self,amount):
        z=self.amount+amount
        self.amount=z
        
        
    def __repr__(self):
       return f'Account(Account_id={self.account_id},  Amount={self.amount})'

if __name__=="__main__":
 b1=bank()
 account_1=account(1000,1)
 account_2=account(20000,2)
 b1.add_account(account_1)
 b1.add_account(account_2)
 b1.accounts[0].withdraw(10000)
 b1.accounts[1].withdraw(10000)
 print(b1.accounts[0])
 print(b1.accounts[1])
    
    
