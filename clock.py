import tkinter
import time
gui = tkinter.Tk()
gui.title("Clock")
gui.geometry("650x150")

def tijd():
    current_time = time.strftime("%H:%M:%S")
    clock.configure(text= current_time)
    clock.after(200,tijd)

clock = tkinter.Label(
    gui,
    font=("Symbol",120),
    bg="black",
    fg="red",

)
clock.pack(
    fill="both",
    padx=0,
    pady=0,
    expand=True
)

tijd()
gui.mainloop()