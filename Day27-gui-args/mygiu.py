import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=550, height=300)


mylabel = tkinter.Label(text="Isioma is my baby girl", font=("Arial", 24, "bold"))
mylabel.pack(side="left", expand=True)


window.mainloop()
