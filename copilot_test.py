import tkinter as tk
from urllib.request import urlopen
import requests
import pandas as pd
import io
import base64
def main():   
   #Create a gui that allows the user to enter a pokemon name and display the sprite for that pokemon
    import tkinter as tk
    import requests
    import pandas as pd
    root = tk.Tk()
    root.title('Pokemon')
    root.geometry('500x300')
    lbl_pokemon = tk.Label(root, text='Enter a pokemon name:')
    lbl_pokemon.grid(row=0, column=0, padx=20, pady=20)
    ent_pokemon = tk.Entry(root, width=30)
    ent_pokemon.grid(row=0, column=1, columnspan=2, padx=20, pady=20)
    btn_get_pokemon = tk.Button(root, text='Get Pokemon', command=lambda: get_pokemon(ent_pokemon.get(),root))
    btn_get_pokemon.grid(row=1, column=1, padx=10, pady=10)
    root.mainloop()

def get_pokemon(name,root):
        url = 'https://pokeapi.co/api/v2/pokemon/' + name
        response = requests.get(url)
        data = response.json()
        sprite = data['sprites']['front_default']
        #get the sprite for the pokemon from url in sprite and display it
        image_byt = urlopen(sprite).read()
        image_b64 = base64.encodebytes(image_byt)
        img = tk.PhotoImage(data=image_b64)
        lbl_pokemon = tk.Label(root, image=img)
        lbl_pokemon.image = img
        lbl_pokemon.grid(row=2, column=1, padx=20, pady=20)
        
main()