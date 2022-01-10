import tkinter  as tk

root = tk.Tk()
root.title('Hello')
root.geometry('300x200')
root.configure(bg='yellow')

box1 = tk.Label(root, text='Hello tkinter', bg='green', fg='blue',)
box1.config(width=15,height=10)
box1.config(font=('Courier',15))

box1.pack()
ipadx=10
ipady=10

root.mainloop()