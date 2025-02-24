class shopping_cart():
    def __init__(self):
        self.pnum=0
        self.products={}
        
    def add_product(self,product):
        self.pnum+=1
        self.products[product.productid]=product.info
    
    def remove_product(self,product):
        self.pnum-=1
        del   self.products[product.productid]
    def  __sub__(self,other):
       if self.pnum > other.pnum :
           i=0
           while i <=  self.pnum:
              for l, k in self.products.items():
                  for t in other.products.values:
                     if k is  t:
                       self.products.pop(l)
                       self.pnum-=1
              i=i+1 
           
       if self.pnum < other.pnum :
           i=0
           while i <=  other.pnum:
              for l, k in other.products.items():
                for t in self.products.values():  
                  if k is t:
                       other.products.pop(l)               
                       other.pnum -=1
              i=i+1         
    def  __add__(self,other):
       self.products.update(other.products)
       self.pnum+=other.pnum
    
    def __repr__(self):
        return f'Shopping_cart({self.pnum},{self.products})'
    
        
        
        



class product():
    def __init__(self,name,price,productid):
        self.name=name
        self.price=price
        self.productid=productid
        self.info={'Name':self.name,'price':self.price,'productid':self.productid}
    
    def __repr__(self):
        return f'product({self.name},{self.price},{self.productid})'
    
    
        
if __name__=='__main__':
    x=product("sprite",20,1)
    l=product("shoes",100,3)
    p=product("lags",10,5)
    y=product("aata",50,2)
    z=shopping_cart()
    z.add_product(x)
    z.add_product(y)
    k=shopping_cart()
    k.add_product(l)
    k.add_product(x)
    k.add_product(y)
    t=z-k
    print(k)
    
        