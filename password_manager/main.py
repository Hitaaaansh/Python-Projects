from tkinter import *
from tkinter import messagebox
import pandas,random,pyperclip,json
def genrate_pass():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list=[random.choice(letters) for char in range(nr_letters)]
    symbols_list=[random.choice(symbols)for char in range(nr_symbols)]
    numbers_list=[random.choice(numbers)for char in range(nr_numbers)]

    password_list=letters_list+symbols_list+numbers_list

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END,password)
    pyperclip.copy(password)


def save():
    website_data=website_entry.get()
    username_data=username_entry.get()
    password_data=password_entry.get()
    # is_ok=messagebox.askokcancel(title=website_data,message=f"The details are \n username:{username_data}\n password:{password_data}\n do you want to save?")
    if len(website_data)!=0 and len(password_data)!=0:
        # if is_ok:
        data={"Website":[website_data],"Username":[username_data],"Password":[password_data]}
        df=pandas.DataFrame(data)
        df.to_csv("password_manager.csv", header=False,mode="a",index=False)
        pandas.read_csv("password_manager.csv")
        json_dict={
            website_data:{
                "Username":username_data,
                "Password":password_data
            }
        }
        try:
            with open("password_manager.json", mode="r")as json_file:
                data=json.load(json_file)

                data.update(json_dict)


            with open("password_manager.json",mode="w")as json_file:
                json.dump(data,json_file,indent=4)
        except FileNotFoundError:
            with open("password_manager.json",mode="w") as json_file:
                json.dump(json_dict,json_file,indent=4)
                
        website_entry.delete(0,END)
        password_entry.delete(0,END)
        website_entry.focus()
        messagebox.showinfo(title="Alert", message="Info saved")

        # else:
        #     website_entry.delete(0,END)
        #     password_entry.delete(0,END)
        #     website_entry.focus()
        #     messagebox.showinfo(title="Alert", message="Info Not Saved")
    else:
        messagebox.showerror(title="Alert",message="Enter Details first")


def search():
    try:
        website_search=website_entry.get()
        with open("password_manager.json",mode="r") as json_file:
            data=json.load(json_file)
            if website_search in data:
                messagebox.showinfo(message=f"Email:{data[website_search]["Username"]}\nPassword:{data[website_search]["Password"]}\n*Password is copied on clipboard")
                pyperclip.copy(data[website_search]["Password"])
            else:
                messagebox.showerror(message="Website is not in the list")
    except (FileNotFoundError,json.JSONDecodeError):
        with open("password_manager.json", "w") as file:
            json.dump({}, file)
        
        messagebox.showerror(message="No Data in file")        



window=Tk()
window.title("Password Manager")
window.config(padx=40,pady=40)
main_screen=Canvas(width=200,height=200)
logo=PhotoImage(file="logo.png")
main_screen.create_image(100,100,image=logo)
main_screen.grid(row=0,column=1,columnspan=1)#change

website=Label(text="Website Name")
website.grid(row=1,column=0,columnspan=1)
website_entry=Entry(width=30)
website_entry.grid(row=1,column=1,columnspan=1)
website_search=Button(text="Search",fg="black",bg="blue",command=search)
website_search.grid(row=1,column=2,columnspan=1)
username=Label(text="Username/Email:")
username.grid(row=2,column=0,columnspan=1)
username_entry=Entry(width=35)
username_entry.insert(END,"hitanshjain1011@gmail.com",)
username_entry.grid(row=2,column=1,columnspan=2)
password=Label(text="Password:")
password.grid(row=3,column=0,columnspan=1)
password_entry=Entry(width=18)
website_entry.focus()
password_entry.grid(row=3,column=1,columnspan=1)
password_button=Button(text="Genrate Password",command=genrate_pass)
password_button.grid(row=3,column=2,columnspan=1)
save_button=Button(text="Save Password",width=35,command=save)
save_button.grid(row=4,column=1,columnspan=2)
window.mainloop()