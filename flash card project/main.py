from tkinter import *
import pandas,random
BACKGROUND_COLOR = "#B1DDC6"
CARD_COLOR="#91c2af"
window=Tk()
try:
    data=pandas.read_csv("data/remaining_learn.csv")
except FileNotFoundError:
    data=pandas.read_csv("data/french_words.csv")
    

list=data.to_dict(orient="records")
    
flip_timer=None
def new_learn_word():
    global word,flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)  

    #the timer everytime starts a new countdown so we have to cancel it after storing it 

    random_word=random.choice(list)
    word=random_word
    main_card.itemconfig(card_image,image=flash_front)
    main_card.itemconfig(word_text,text=word["French"],fill="black")
    main_card.itemconfig(language_text,text="French",fill="black")
    flip_timer=window.after(3000,swap_card)

def tick_card():
    global data
    list.remove(word)
    new_learn_word()
    remaining_learn=pandas.DataFrame(list)
    remaining_learn.to_csv("data/remaining_learn.csv", index=None)


def swap_card():
    main_card.itemconfig(card_image,image=flash_back)
    main_card.itemconfig(language_text,text="English",fill="white")
    main_card.itemconfig(word_text,text=word["English"],fill="white")

window.title("Flash Card App")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
main_card=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
flash_front=PhotoImage(file="images/card_front.png")
flash_back=PhotoImage(file="images/card_back.png")
card_image=main_card.create_image(400,263,image=flash_front)
main_card.grid(row=0,column=0,columnspan=2)

language_text=main_card.create_text(400,150,text="French",font=("ariel",40,"italic"))
word_text=main_card.create_text(400,263,text="French",font=("ariel",60,"bold"))

correct=PhotoImage(file="images/right.png")
wrong=PhotoImage(file="images/wrong.png")
got_it=Button(image=correct,highlightthickness=0,border=0,command=tick_card)
got_it.grid(row=1,column=0)
pardon=Button(image=wrong,highlightthickness=0,borderwidth=0,command=new_learn_word)
pardon.grid(row=1,column=1)
new_learn_word()

window.mainloop()

