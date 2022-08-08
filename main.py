from tkinter import *
import math

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
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    checkmarks_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Are you working?")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# Cannot be a loop, cause otherwise program would never reach the mainloop below.
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # ***!!!*** => This is possible because Python is a STRONGLY, DYNAMICALLY TYPED LANGUAGE.

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1) # count-1 corresponds to "count" in the function declaration
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        checkmarks_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 112, text="00:00", font=("Roboto", 35, "bold"))
canvas.grid(column=1, row=1)


title_label = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)


start_button = Button(text="Start", command=start_timer, bd=0, bg=YELLOW)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, bd=0, bg=YELLOW)
reset_button.grid(column=2, row=2)

checkmarks = []
checkmarks_label = Label(font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
checkmarks_label.grid(column=1, row=3)



# Last line
window.mainloop()
