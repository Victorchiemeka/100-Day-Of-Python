from tkinter import *

# Create the main window
window = Tk()
window.title("My first GUI")
window.minsize(width=550, height=300)


mylabel = Label(text="Label")
mylabel.grid(column=0, row=0)

button = Button(text="New Button")
button.grid(column=3, row=0)

second = Button(text="Button")
second.grid(column=2, row=2)


third = Entry(width=10)
third.grid(column=1, row=0)

window.mainloop()
