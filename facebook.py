'''in this window code is writeen for html hyperlink'''

from tkinter import *
from tkhtmlview import HTMLLabel #view as html file
import subprocess 

root = Tk()
root.geometry("400x400")
root.wm_iconbitmap("facebook.ico")
root.title("facebook")
 

my_label = HTMLLabel(root, html="""
<li> LINK FOR FACEBOOK</LI>
    <ul>
        <li><a href='https://www.facebook.com//'>Facebook</a></li>
       
    </ul>
    """)
 
my_label.pack(pady=20, padx=20)


# function for home button

def run_home():

    root.destroy()
    subprocess.call(["python","project.py"])



b=Button(root,text="⌂ home",bg="black",fg="white",command=run_home)
b.place(x=180,y=250)
 
root.mainloop()