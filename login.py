from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox
import subprocess

#============== Main Window ===============



root=Tk()
root.title("LOGIN")
root.geometry('400x580')
root.resizable(FALSE, FALSE)
root.config(bg="#111d5e")

conn=sqlite3.connect('register.db')

c=conn.cursor()

#######table

# c.execute(""" CREATE TABLE login (
        
#         name String NOT NULL,
#         username String PRIMARY KEY,
#         address String NOT NULL,
#         DOB Integer NOT NULL,
#         password String NOT NULL,


#         )""")

def run_register():
   root.destroy()
   subprocess.call(["python","register.py"])

def run_login():
    root.destroy()
    subprocess.call(["python","login.py"])

def run_admin():
   root.destroy()
   subprocess.call(["python","admin.py"])

def open(user):
   
   root.destroy()
   subprocess.call(["python","project.py", "--user", user[1]])
   

def login():

   conn=sqlite3.connect('register.db')    
   c=conn.cursor()

   c.execute('SELECT * FROM login WHERE username = ? AND password = ?',(username_entry.get(),password_entry.get()))
   # print(c.fetchone())
   print(username_entry.get())
   user = c.fetchone()

   if username_entry.get()=="admin" and password_entry.get()=="admin":

      run_admin()

   while not user:

      messagebox.showerror("Invalid","Invalid username or password")

      run_login()

      c.execute('SELECT 1 FROM login WHERE username = ? AND password = ?',(username_entry.get(),password_entry.get()))


   
   else:
      
      open(user)


login_text_label=Label(root,text="LOGIN",font=(Canvas,30),bg="#111d5e",relief=GROOVE,fg="maroon",borderwidth=6)
login_text_label.place(x=120,y=15)

username_label=Label(root,text="Username:",font=(Canvas,12),bg="#111d5e",fg="red")
username_label.place(x=4,y=270)
username_entry=Entry(root,font=Canvas,width=35,bg="white",fg="red")
username_entry.place(x=4,y=300)

password_label=Label(root,text="Password:",font=(Canvas,12),bg="#111d5e",fg="red")
password_label.place(x=4,y=330)
password_entry=Entry(root,font=Canvas,width=35,bg="white",fg="red")
password_entry.place(x=4,y=360)

forget_password_button=Button(root,text="forget password ?",borderwidth=0,fg="green",bg="#111d5e")
forget_password_button.place(x=280,y=390)

login_button=Button(root,text="login",borderwidth=4,command=login,bg="green",fg="white",relief=GROOVE,width=15)
login_button.place(x=155,y=440)


or_register_label=Label(root,text="or register using,",bg="#111d5e",fg="red")
or_register_label.place(x=170,y=500)

signup_button=Button(root,text="signup",borderwidth=4,command=run_register,relief=GROOVE,bg="maroon",width=15,fg="white")
signup_button.place(x=155,y=550)


image1=Image.open("login.png")
image1=image1.resize((150,150),(Image.ANTIALIAS))
image1=ImageTk.PhotoImage(image1)

load_img=Label(root,image=image1,bg="#111d5e")
load_img.place(x=110,y=100)

conn.commit()
conn.close()
root.mainloop()