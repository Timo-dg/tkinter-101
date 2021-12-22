import tkinter
window = tkinter.Tk()
window.title('My First Window')
grote = 150
y = 0
colors = ('white', 'blue', 'green', 'red', 'yellow', 'black')
z = len(colors)

def changer():
    global grote, window, y, z 
    if z != 0:
        window.geometry(str(grote) +'x'+ str(grote))
        grote = int(grote) +50
        window.configure(bg=colors[y])
        y = y + 1
        print(z)
        z = z - 1
    else:
        print('Boom!')
        window.destroy()

for x in range(0,len(colors) + 1):
    window.after(x* 2000, changer)

window.mainloop()