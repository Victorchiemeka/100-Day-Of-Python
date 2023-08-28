from tkinter import *
from math import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timetxt, text="00:00")
    firsttext.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        firsttext.config(text="Long Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break)
        firsttext.config(text="Break", fg=PINK)

    else:
        count_down(work_sec)
        firsttext.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timetxt, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_time()
        marks = ""
        work_session = floor(reps / 2)
        for _ in range(work_session):
            marks += "✅"
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

firsttext = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
firsttext.grid(column=1, row=0)


canvas = Canvas(width=280, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timetxt = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)


start_button = Button(
    text="Start",
    highlightthickness=0,
    command=start_time,
    bg=GREEN
    # command=miles_to_km, bg="red", fg="white"
)  # Set Button colors
start_button.grid(column=0, row=2)

reset_button = Button(
    text="reset",
    highlightthickness=0,
    command=reset_timer,
    bg=RED,  # bg="red", fg="white"
)  # Set Button colors
reset_button.grid(column=2, row=2)

check = Label(text="")  # bg=YELLOW)
check.grid(column=1, row=3)

window.mainloop()
