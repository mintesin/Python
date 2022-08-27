from tkinter import *
from PasswordGenerate import generate_password
from tkinter import messagebox
import pyperclip
#PASSWORD GENERATION
def pasword_geenration():
    password=generate_password()
    pyperclip.copy(password)
    # print(password)
    password_entry.insert(0,password)
    return password

#SAVING THE PASSWORD
def save_password():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    if len(website)==0:

        messagebox.showinfo(title='OOps',message='Please fill the entries')
    else:
        is_ok=messagebox.askokcancel(title=website,message='Have you finished entering?')
        if is_ok:

            with open('data.txt','a') as file:
                file.write(f'{website}|')
                # file.write(f'{email}|')
                file.write(f'{password}')
                file.write(f'\n')
                website_entry.delete(0,END)
                email_entry.delete(0,END)
                password_entry.delete(0,END)




# GENERATING THE WINDOW
window=Tk()
window.title("Password Manager")
# window.minsize(width=300,height=300)
window.config(padx=50,pady=50,bg='black')

canvas=Canvas(width=200,height=200)
photo=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=photo)
canvas.grid(column=1,row=0)


web_label=Label(text='Website: ')
web_label.grid(column=0,row=1)


generate_pass=Button(text='Generate Password',command=pasword_geenration)
generate_pass.grid(column=2,row=4,columnspan=1)

add_button=Button(text='Add',width=36,command=save_password)
add_button.grid(column=1,row=6,columnspan=2)
emus=Label(text="Email/UserName: ")
emus.grid(column=0,row=2)
Pass_label=Label(text="Password: ")
Pass_label.grid(column=0,row=4)

website_entry=Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

email_entry=Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
# email_entry.focus()

email_entry.insert(0,'mintd060@gmail.com')
password_entry=Entry(width=21)
password_entry.grid(column=1,row=4)
# option_label=Label(text="Fill your password or click on generate button: ")
# option_label.grid(column=1,row=3)








window.mainloop()
