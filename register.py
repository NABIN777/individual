from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox
import subprocess
from tkcalendar import calendar_
from tkcalendar.dateentry import DateEntry

root=Tk()
root.title('Register')
root.geometry('400x580')
root.resizable(False, False)
root.config(bg="#111d5e")

#----------------------------------DATABASE---------------------------------------


conn=sqlite3.connect('register.db')

c=conn.cursor()

######table

# c.execute(""" CREATE TABLE login (
        
#         name String NOT NULL,
#         username String PRIMARY KEY,
#         address String NOT NULL,
#         password String NOT NULL,


#         )""")
def run_register():
   root.destroy()
   subprocess.call(["python","register.py"])



def run_login():
    root.destroy()
    subprocess.call(["python","login.py"])


def register():
    
    conn=sqlite3.connect('register.db')

    c=conn.cursor()

    c.execute('SELECT 1 FROM login WHERE username = ?',(usernamer_entry.get(),))

    while len(c.fetchall()) > 0:

        messagebox.showerror("Error","Username already exists")
        
        run_register()

        c.execute('SELECT 1 FROM login WHERE username = ?',(usernamer_entry.get(),))


    c.execute("INSERT INTO login VALUES(:name, :username, :address, :password)",
        
                {
                    "name": name_entry.get(),
                    "usernamer": usernamer_entry.get(),
                    "address": address_entry.get(),
                    "password": password_entry.get(),
                    
                }
        
        )
    
    messagebox.showinfo("register","register sucessfully")
    
    name_entry.delete(0,END)
    usernamer_entry.delete(0,END)
    address_entry.delete(0,END)

    password_entry.delete(0,END)

    conn.commit()
    conn.close()
    
    run_login()

register_text_label=Label(root,text="CREATE ACCOUNT",font=(Canvas,25),bg="#111d5e",fg="dark red",relief=GROOVE,borderwidth=4)
register_text_label.place(x=55,y=15)


name_label=Label(root,bg="#111d5e",text="Name:",font=(Canvas,12),fg="red")
name_label.place(x=4,y=250)
name_entry=Entry(root,font=Canvas,width=35,bg="white")
name_entry.place(x=4,y=275)

usernamer_label=Label(root,bg="#111d5e",text="Username:",font=(Canvas,12),fg="red")
usernamer_label.place(x=4,y=305)
usernamer_entry=Entry(root,font=Canvas,width=35,bg="white")
usernamer_entry.place(x=4,y=330)

address_label=Label(root,bg="#111d5e",text="Address:",font=(Canvas,12),fg="red")
address_label.place(x=4,y=360)
address_entry=Entry(root,font=Canvas,width=35,bg="white")
address_entry.place(x=4,y=385)


DOB_label=Label(root,bg="#111d5e",text="DOB:",font=(Canvas,12),fg="red")
DOB_label.place(x=4,y=415)
DOB_entry=DateEntry(root,width=61,date_pattern="dd/mm/Y",bg="grey")
DOB_entry.place(x=4,y=440,height=30)

password_label=Label(root,bg="#111d5e",text="Password:",font=(Canvas,12),fg="red")
password_label.place(x=4,y=470)
password_entry=Entry(root,font=Canvas,width=35,bg="white")
password_entry.place(x=4,y=495)


register_button=Button(root,text="Sign Up",bg="green",borderwidth=4,command=register,relief=GROOVE,fg="WHITE",width=20)
register_button.place(x=110,y=530)

# logo image

image1=Image.open("signup.png")
image1=image1.resize((150,150),(Image.ANTIALIAS))
image1=ImageTk.PhotoImage(image1)

load_img=Label(root,image=image1,bg="grey")
load_img.place(x=125,y=75)


conn.commit()
conn.close()

root.mainloop()
