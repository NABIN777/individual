from tkinter import *
import sqlite3

root=Tk()
root.title("Customer details")
root.geometry('400x580')
root.resizable(FALSE, FALSE)

conn=sqlite3.connect('register.db')

c=conn.cursor()

#######table

# c.execute(""" CREATE TABLE login(
        
#         name String NOT NULL,
#         username String PRIMARY KEY,
#         email String NOT NULL,

#         password String NOT NULL

#         )""")







conn.commit()
conn.close()


root.mainloop()