from tkinter import *

window = Tk()
window.title("Miles to Kilometer converter")
window.config(padx=20, pady=20, bg="green")  # Set background color to green

third = Entry(width=10, bg="white", fg="black")  # Set Entry colors
third.grid(column=1, row=0)

mylabel = Label(text="Miles", bg="green", fg="white")  # Set Label colors
mylabel.grid(column=2, row=0)

equal = Label(text="is equal", bg="green", fg="white")  # Set Label colors
equal.grid(column=0, row=1)

number = Label(text="0", bg="green", fg="white")  # Set Label colors
number.grid(column=1, row=1)

km = Label(text="km", bg="green", fg="white")  # Set Label colors
km.grid(column=2, row=1)


def miles_to_km():
    kilo = float(third.get()) * 1.60934
    final = round(kilo)
    number["text"] = f"{final}"


button = Button(
    text="Calculate", command=miles_to_km, bg="red", fg="white"
)  # Set Button colors
button.grid(column=1, row=2)

window.mainloop()
