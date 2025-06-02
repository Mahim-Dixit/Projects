from tkinter import *
from tkinter import Tk
from PIL import Image,ImageTk

class pokemon_GUI(Tk):
   def __init__(self):
          super().__init__()
          self.image=[]
   def Imgloader(self,fp,size):
        bg=Image.open(fp).resize(size)
        image=ImageTk.PhotoImage(bg)
        self.image.append(image)
        return image
 






    
if __name__=="__main__":
    root= pokemon_GUI()
    root.geometry("500x500")
    x=root.Imgloader('Profesor_Oak_Pokémon_Am.png',(500,500))
    l1=Label(root,image=x)
    
    l1.pack()
    root.mainloop()