from tkinter import *
from tkhtmlview import HTMLLabel
import subprocess 

root = Tk()
root.geometry("400x400")
root.title("google")
root.wm_iconbitmap("google.ico")
 

my_label = HTMLLabel(root, html="""
<li> LINK FOR Google</LI>
    <ul>
        <li><a href='https://www.google.com//'>Google</a></li>
       
    </ul>
    """)
 
my_label.pack(pady=20, padx=20)


def run_home():

    root.destroy()
    subprocess.call(["python","project.py"])



b=Button(root,text="⌂ home",bg="black",fg="white",command=run_home)
b.place(x=180,y=250)
 

 
root.mainloop()