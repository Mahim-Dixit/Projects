import os
import shelve
class users () :
    def __init__(self):
        self.name=str(input("Enter your name : "))
        self.trainer_id=None
        self.badges=None
    def Get_info(self) :
        
        self.trainer_id=str(input("Enter your trainer_id : "))
        self.badges=int(input("Enter your badges : "))
    def print_info(self):
        print(f" Name : {self.name} \n trainer id :{self.trainer_id} \n badges : {self.badges} \n")
    def make_user(self) :
        details=[self.name,self.trainer_id,self.badges]
        sfile=shelve.open('trainers')
        sfile[self.name]=details
        sfile.close()
    def get_user(self):
        sfile=shelve.open('trainers')
        x=sfile[self.name]
        self.name=x[0]
        self.trainer_id=x[1]
        self.badges=x[2]
        sfile.close()
    
        
    
                
            
        
if __name__=='__main__' :
    
  user1=user()
  user1.print_information()
