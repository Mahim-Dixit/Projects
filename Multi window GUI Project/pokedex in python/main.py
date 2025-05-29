from pokedex import pokemon
from user import users

print("***Welcome to the world of pokemon***")
x=int(input((f"Are you a New Trainer : \n 1.YES \n 2.NO \n ")))
if x == 1 :
    y=users()
    y.Get_info()
    y.make_user()
    print("***You found a pokemon***")
    z=pokemon()
    z.get_photo()
    z.print_info()
    
elif x == 2 :
    y=users()
    y.get_user()
    print("***You found a pokemon***")
    z=pokemon()
    z.get_photo()
    z.print_info()

print("Your Info ")
y.print_info()
    
