import tkinter

# Create the main window
window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=550, height=300)

# Create a label
mylabel = tkinter.Label(text="Isioma is my baby girl", font=("Arial", 24, "bold"))
mylabel.pack()

# Update label's text
mylabel["text"] = "Emeka must shine"


# Button click function
def clicked():
    print("Button got clicked")
    mylabel["text"] = input_widget.get()


# Create a button
button = tkinter.Button(text="Click Me", command=clicked)
button.pack()

# Entry widget for input
input_widget = tkinter.Entry(width=10)
input_widget.pack()


# Start the GUI event loop
window.mainloop()
