import csv
import os
from PIL import Image
class pokemon() :
    def __init__(self):
        self.name=str(input("which pokemon you are looking at "))
        self.get_info()

    def get_info(self):
        fileobj=open('pokemon.csv')
        Reader=csv.reader(fileobj)
        for row in Reader :
          if self.name == row[1] :
              self.type1= row[2]
              self.type2=row[3]
              self.total=row[4]
              self.HP   =row[5]
              self.attack=row[6]
              self.defence=row[7]
              self.sp_atk=row[8]
              self.sp_def=row[9]
              self.speed=row[10]
              self.generation=row[11]
              self.legendary=row[12]
        fileobj.close()      
    def print_info(self) :
         print(f"Name : {self.name} \n Type1 : {self.type1} \n Type2 : {self.type2} \n Total : {self.total} \n HP : {self.HP} \n Attack : {self.attack} \n Defence : {self.defence} \n Sp_Atk : {self.sp_atk} \n Sp_Def : {self.sp_def} ")
         print(f"Speed : {self.speed} \n Generation : {self.generation} \n Legendary : {self.legendary} \n")
    def get_photo(self) :
        os.chdir(r'.\pokemon-images-dataset-by-type-master\pokemon-images-dataset-by-type-master\all')
        im = Image.open(self.name+".png")
        im.show()
        
        


if __name__== '__main__':   
           
  p=pokemon()
  p.get_photo()
 
         
    
    
