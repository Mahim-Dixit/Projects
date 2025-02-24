from tkinter import *
from tkinter import Tk
from PIL import Image,ImageTk
import GUI_tools
import pandas as pd



global info_fields
global info
names=[]
gender=[]
pokemons=[]
info_fields=[]
info=[]
global frame4
global frame1
global screen3

global name
global isboy
global Pokemon
def Identity_page():
    screen2=Toplevel(root)
    screen2.geometry("700x700")
    global isboy
    isboy=BooleanVar()
    l1=Label(screen2,text="Are you a boy or girl?",font=("Comic-Sans","18","bold"),fg="red")
    l2=Label(screen2,image=root.Imgloader("Pokemon-Pokeball-PNG-File.png",(450,450)))
    l1.place(x=250,y=20)
    l2.place(relx=0.25,rely=0.2)
    b1=Button(screen2,image=root.Imgloader("boy.jpg",size=(150,300)),command=boy_set)
    b1.place(relx=0.05,rely=0.35)
    b2=Button(screen2,image=root.Imgloader("girl.jpg",size=(150,300)),command=girl_set)
    b2.place(relx=0.75,rely=0.35)
    frame1=Frame(screen2,bg="red")
    frame1.place(relx=0.25,rely=0.89)
    global name
    name=StringVar()
    namelabel=Label(frame1,text="name",font=("comic-sans","18"),fg="red")
    
    entry1=Entry(frame1,font=("comic-sans","18"),textvariable=name)
    b3=Button(frame1,text="Enter",font=("comic-sans","18"),command=save_name)
    namelabel.grid(row=0,column=0)
    entry1.grid(row=0,column=1)
    b3.grid(row=0,column=2)
    b4=Button(frame1,image=root.Imgloader("pokeball.256x256.png",size=(50,50)) ,command=Search_page)
    b4.grid(row=1, column=1)
    screen2.mainloop()
    gender_check()
    
    
    
def boy_set():
    global isboy
    isboy.set(True)

def girl_set():
    global isboy
    isboy.set(False)
    
def gender_check():
     global isboy
     if isboy.get()==True :
         gender.append("boy")
     if isboy.get()==False :
         gender.append("girl")
         
def seek_pokemon(pokemon):
    global info
    global info_fields
    x=pd.read_csv("pokemon.csv")
    for i in x.index:
      if x.loc[i]["Name"]==pokemon.title():
       data=list(x.loc[i].index)
       data1=list(x.loc[i].values)
       info_fields=data
       info=data1
       x=lambda :create_frame(pokemon)
       x()

def create_frame(pokemon_name):
    
    global screen3
    global frame4
    
    frame4=Frame(screen3)
    frame4.place(relx=0.01,rely=0.55)
    labels=[]
    labels2=[]
    for i in info_fields:
        label=Label(frame4,text=f"{i}",font=("comic-sans","18"),fg="red")
        labels.append(label)
    for i in info :
         label=Label(frame4,text=f"{i}",font=("comic-sans","18"),fg="red")
         labels2.append(label)
        
    for i,label in enumerate(labels):
        label.grid(row=0,column=i)
    for i,x in enumerate(labels2):
        x.grid(row=1,column=i)
    label2=Label(frame4,image=root.Imgloader(f"./pokemon-images-dataset-by-type-master/pokemon-images-dataset-by-type-master/all/{pokemon_name.lower()}.png",(150,150)))
    label2.grid(row=2,column=7)
    b2=Button(frame1,image=root.Imgloader("pokeball.256x256.png",size=(50,50)) ,command=Delete_frame4)
    b2.grid(row=1 ,column=0)
       
def Delete_frame4():
     global frame4
     frame4.destroy()        
        


        

       
    
     
    




         
def save_pokemon():
    global Pokemon
    data=Pokemon.get()
    pokemons.append(data)
    
    seek_pokemon(data)
    Pokemon.set(" ")
 
    
 
def save_name():
    global name
    data=name.get()
    names.append(data)
    name.set(" ")
    
        


def Search_page():
    global frame1
    global screen3
    global frame4
    screen3=Toplevel(root)
    screen3.geometry("1100x700")
    label1=Label(screen3,text=f"Hi {names[0]}",fg="red",font=("Comic-sans MS","18","bold"))
    l2=Label(screen3,image=root.Imgloader("Pokemon-Pokeball-PNG-File.png",(450,450)))
    label2=Label(screen3,text="you found a pokemon",fg="red",font=("Comic-sans MS","18","bold"))
    global Pokemon
    Pokemon=StringVar()
    label2.place(relx=0.25,rely=0.2)
    l2.place(relx=0.25,rely=0.2)
    label1.place(x=250,y=0)
    frame1=Frame(screen3,bg="red",width=700,height=100)
    frame1.place(relx=0.20,rely=0.4)
    E1=Entry(frame1,textvariable=Pokemon,font=("comic-sans","18","bold"),width=10)
    E1.grid(row=0,column=1)
    L3=Label(frame1,text="Pokemon_name",font=("comic-sans","18","bold"),fg="white",bg="red")
    L3.grid(row=0,column=0)
    b1=Button(frame1,image=root.Imgloader("pokeball.256x256.png",size=(50,50)) ,command=save_pokemon)
    b1.grid(row=0,column=2)
    
    
    screen3.mainloop()
    print(info)

    


root=GUI_tools.pokemon_GUI()
root.geometry("500x550")
l1=Label(root,image=root.Imgloader("Pokemon-Pokeball-PNG-File.png",(450,450)))
l2=Label(root,text="Welcome to the world of pokemon",font=("Comic-Sans","18","bold"),fg="red")
l3=Label(root,image=root.Imgloader("Profesor_Oak_Pokémon_Am.png",size=(90,90)))

b1=Button(root,image=root.Imgloader("pokeball.256x256.png",size=(50,50)) ,command=Identity_page)



l1.grid(row=1,column=0)
l2.grid(row=0,column=0)
l3.grid(row=1,column=0)
b1.grid(row=2,column=0)

root.mainloop()
