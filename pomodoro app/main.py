from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
REPS=8
timing=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_but():
    global REPS
    window.after_cancel(timing)
    REPS=8
    start_button.config(state="normal")
    canvas.itemconfig(tom_text,text="00:00")
    checkmark.config(text=" ")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_func():
    start_button.config(state="disabled")
    global REPS
    REPS-=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if REPS==0:
        count_down(long_break_sec)
        text.config(text="Long break")
    elif REPS%2==0:
        count_down(short_break_sec)
        text.config(text="short break")

    else:
        count_down(work_sec)
        text.config(text="WORK")
        

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timing
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(tom_text,text=f"{count_min}:{count_sec}")
    if count>0:
      timing= window.after(1000,count_down,count-1)
    else:
        start_func()
        if REPS%2==0:
            no_of_task=math.floor((8-REPS)/2)
            mark="✔️"*no_of_task
            checkmark.config(text=mark)
        else:
            pass

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

text=Label(text="TIMER",bg=YELLOW,fg=GREEN,font=(FONT_NAME,40,"bold"))
text.grid(row=0,column=1)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
Tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=Tomato)
tom_text=canvas.create_text(100,125,text="00:00", fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)

start_button=Button(text="Start",fg=GREEN,command=start_func)
start_button.grid(row=2,column=0)

reset_button=Button(text="Reset",fg=GREEN, command=reset_but)
reset_button.grid(row=2,column=2)

checkmark=Label(text=" " ,fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
checkmark.grid(row=4,column=1)


window.mainloop()