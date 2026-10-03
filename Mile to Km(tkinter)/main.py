import tkinter as tk

def converter():
    miles=int(input.get())
    kilom=int(miles*1.609)
    km.config(text=f"{kilom}")




window=tk.Tk()
window.title("Miles to Km")
window.config(padx=30,pady=30)

label=tk.Label(text="Miles")
label.grid(column=0,row=0)

input=tk.Entry(width=10)
input.insert(tk.END,string="0")
input.grid(column=1,row=0)


label_2=tk.Label(text="is equal to")
label_2.grid(column=0,row=1)

km=tk.Label(text="0")
km.grid(column=1,row=1)

label_3=tk.Label(text="km")
label_3.grid(column=2,row=1)

button=tk.Button(text="Calculate",command=converter)
button.grid(column=1,row=2)






window.mainloop()