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

def resetTimer():
    window.after_cancel(timer)
    canvas.itemconfig(timerText,text="00:00")
    title.config(text="Timer",fg=GREEN)
    checkMark.config(text="")
    startBtn["state"] = "active"


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global reps
    workSec = WORK_MIN * 60
    shortBreak = SHORT_BREAK_MIN * 60
    longBreak = LONG_BREAK_MIN * 60
    startBtn["state"] = "disabled"
    reps +=1
    if reps % 8 == 0:
        window.focus_force()
        title.config(text="Break",fg=RED)
        countDown(longBreak)
    elif reps % 2 == 0:
        window.focus_force()
        title.config(text="Break",fg=PINK)
        countDown(shortBreak)
    else:
        window.focus_force()
        title.config(text="Work")
        countDown(workSec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(count):
    minutes = math.floor(count / 60)
    seconds = count  % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timerText,text=f"{ minutes}:{seconds}")

    if count >0:
        global timer
        timer = window.after(1000,countDown,count-1)
    else:
        startTimer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks +="✔"
        checkMark.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx = 100,pady = 50,bg=YELLOW)
title = Label(text="Timer",fg=GREEN,font=(FONT_NAME,50,"normal"),bg=YELLOW)
title.grid(column=1,row=0)
canvas = Canvas(width = 200, height = 224,bg=YELLOW,highlightthickness=0)
tomatoImg = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image = tomatoImg)
timerText =  canvas.create_text(100,130, text = "00:00", fill="white", font=(FONT_NAME,35,"bold"))

canvas.grid(column = 1, row=1)

startBtn = Button(text="Start", command =startTimer)
startBtn.grid(column = 0, row=2)


resetBtn = Button(text="Reset",command = resetTimer)
resetBtn.grid(column = 2, row=2)

checkMark = Label(fg=GREEN,bg=YELLOW)
checkMark.grid(column=1,row=3)



window.mainloop()