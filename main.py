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
REPS = 1
worker = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_button():
    window.after_cancel(worker)
    canvas.itemconfig(timer_text_item, text="00:00")
    timer.config(text="TIMER", fg=GREEN)
    checkmark.config(text="")
    global REPS
    REPS = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_button():

    global REPS
    work_sec = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60

    if REPS % 2 == 0 and REPS != 8:
        timer.config(text="BREAK", fg=PINK)
        count_down(short)

    elif REPS == 8:
        timer.config(text="BREAK", fg=RED)
        count_down(long)
    else:
        if REPS > 8:
            reset_button()
        else:
            window.lift()
            window.attributes('-topmost', True)
            window.after_idle(window.attributes, '-topmost', False)
            window.focus_force()

            timer.config(text="WORK", fg=GREEN)
            count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global REPS
    minute = math.floor(count / 60)
    seconds = count % 60

    if minute < 10:
        minute = f"0{math.floor(count / 60)}"

    if seconds < 10:
        seconds = f"0{count % 60}"
        if seconds == 0:
            seconds = "00"

    canvas.itemconfig(timer_text_item, text=f"{minute}:{seconds}")
    if count > 0:
        global worker
        worker = window.after(1000, count_down, count -1)
    else:
        if REPS <= 8 :
            REPS += 1
            start_button()
            marks = ""
            work_session = math.floor(REPS/2)
            for i in range(work_session):
                marks += "✓"
            checkmark.config(text=marks)
        else:
            reset_button()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.minsize(width=500, height=450)
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)
timer_text_item = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))


timer = Label(text="TIMER", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
timer.grid(column=1, row=0)


start = Button(text="Start", highlightbackground=YELLOW, command=start_button)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightbackground=YELLOW, command=reset_button)
reset.grid(column=2, row=2)


checkmark = Label(font=("Times_New_Roman", 15, "bold"), bg=YELLOW, fg=GREEN)
checkmark.grid(column=1, row=3)

window.mainloop()