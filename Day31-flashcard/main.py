from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
currentcard = {}
tolearn = {}
window = Tk()
window.title("Flash card app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
try:
    data = pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    mymain = pandas.read_csv("data/french_words.csv")
    tolearn = mymain.to_dict(orient="records")
else:
    tolearn = data.to_dict(orient="records")


def randword():
    global currentcard, myafter
    window.after_cancel(myafter)
    currentcard = random.choice(tolearn)
    value = currentcard["French"]

    # english = currentcard["English"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=value, fill="black")
    canvas.itemconfig(img, image=logo_img)
    myafter = window.after(3000, changeimage)


def changeimage():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=currentcard["English"], fill="white")
    canvas.itemconfig(img, image=secondimage)


def create_again():
    canvas.create_image(400, 263, image=logo_img)
    canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
    canvas.create_text(400, 263, text=currentcard["French"], font=("Ariel", 60, "bold"))


def isknown():
    tolearn.remove(currentcard)
    data = pandas.DataFrame(tolearn)
    data.to_csv("data/word_to_learn.csv", index=False)
    randword()


canvas = Canvas(window, height=526, width=800)
logo_img = PhotoImage(file="images/card_front.png")
# logo_img = PhotoImage(file="/images/card_front.png")
img = canvas.create_image(400, 263, image=logo_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
myafter = window.after(3000, changeimage)

secondimage = PhotoImage(file="images/card_back.png")

cross_image = PhotoImage(file="images/wrong.png")
unknown_image = Button(image=cross_image, highlightthickness=0, command=randword)
unknown_image.grid(
    row=1,
    column=0,
)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=isknown)
known_button.grid(row=1, column=1)


randword()
window.mainloop()
