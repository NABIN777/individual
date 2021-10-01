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

#######table

# c.execute(""" CREATE TABLE login(
        
#         name String NOT NULL,
#         username String PRIMARY KEY,
#         adress String NOT NULL,
#         DOB Integer NOT NULL,
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

    c.execute('SELECT 1 FROM login WHERE username = ?',(username_entry.get(),))

    while len(c.fetchall()) > 0:

        messagebox.showerror("Error","Username already exists")
        
        run_register()

        c.execute('SELECT 1 FROM login WHERE username = ?',(username_entry.get(),))


    c.execute("INSERT INTO login VALUES(:name, :username, :adress, :password)",
        
                {
                    "name": name_entry.get(),
                    "username": username_entry.get(),
                    "address": address_entry.get(),
                    "DOB": DOB_entry.get(),
                    "password": password_entry.get(),
                    
                }
        
        )
    
    messagebox.showinfo("register","register sucessfully")
    
    name_entry.delete(0,END)
    username_entry.delete(0,END)
    address_entry.delete(0,END)
    DOB_entry.delete(0,END)
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

username_label=Label(root,bg="#111d5e",text="Username:",font=(Canvas,12),fg="red")
username_label.place(x=4,y=305)
username_entry=Entry(root,font=Canvas,width=35,bg="white")
username_entry.place(x=4,y=330)

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






conn.commit()
conn.close()

root.mainloop()
