# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:50:11 2024

@author: Dixit
"""
class Shopping():
    class product():
        def __init__(self,product_name,info,product_id,category):
            self.product_name=product_name
            self.info=info
            self.product_id=product_id
            self.category=category
        def change_name(self):
           z=input("Enter new name : " )
           self.product_name=z
        def change_category(self):
           z=input("Enter new category : ")
           self.category=z
        def change_product_id(self):
           z=input("Enter new product_id : ")
           self.product_id=z
        def change_info(self):
           z=input("Enter new info : ")
           self.info=z
        
           
            
    class shopping_cart():
        def __init__(self,product,account):
            self.products=[]
            self.account=account
        def add_product(self,product):
            self.products.append(product)
        def remove_product(self,product):
            self.products.remove(product)
        def  __repr__(self):
           return f"Shopping Cart Has {len(self.products)} items "
            
    class account():
        def __init__(self,account_id,password,email):
            self.account_id=account_id
            self.password=password
            self.email=email
        def change_account_id(self):
            z=input("Enter new account_id : ")
        def change_password(self):
            z=input("Enter new password : ")
            self.password=z
        def change_email(self):
            z=input("Enter new email : ")
            self.email=z
        def __repr__(self):
            return f"Account(Id : {self.account_id} \n Password : {self.password} \n Email : {self.email} )"
            
            
            
            
    class account_manager():
        def __init__(self):
            self.accounts=[]
        def add_account(self,account):
            self.accounts.append(account)
        def remove_account(self,account):
            self.account.remove(account)
        def fetch_account(self,account):
            for acc in self.accounts :
                if acc.account_id == account.account_id:
                    break
                return acc
        def __repr__(self):
            return f"There are {len(self.accounts)} accounts"
        
    
    class product_manager():
        def __init__(self):
            self.products=[]
        def add_product(self,product):
            self.products.append(product)
        def remove_product(self,product):
            self.products.remove(product)
        def fetch_product(self,product):
            for pro in self.products:
                if pro.product_id==product.product_id:
                    break
                return pro
        def __repr__(self):
            return f"there are {len(self.products)} products"
    
if __name__=="__main__" :
