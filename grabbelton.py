import tkinter as tk
import random
from tkinter import messagebox

root = tk.Tk()
root.title('Grabbelton')
root.geometry("750x500")

geld = ['1 euro', '5 euro', '10 euro', '50 euro', '100 euro','250 euro','500 euro', '750 euro', '1000 euro','10.000 euro']
gegrabbeld = ''
counter = 10

def grabbel():
    global gegrabbeld, counter
    gegrabbeld = random.choice(geld)
    geld.remove(gegrabbeld)
    counter -= 1
    Frame = tk.Label(
        root,
        text='Gefeliciteerd, je hebt '+ (gegrabbeld) +' gegrabbeld! er zijn nog '+ str(counter) +' prijzen over'
    )
    messagebox.showwarning('Geld','Gefeliciteerd, je hebt '+ (gegrabbeld) +' gegrabbeld!')
    Frame.pack()

button = tk.Button(
    text=('Grabbel'),
    font=('Arial', 50,'bold'),
    command=grabbel
)
button.pack()

root.mainloop()