from tkinter import *
from tkhtmlview import HTMLLabel
 

root = Tk()
root.geometry("400x400")
 

my_label = HTMLLabel(root, html="""
<li> LINK FOR Google</LI>
    <ul>
        <li><a href='https://www.google.com//'>Google</a></li>
       
    </ul>
    """)
 
my_label.pack(pady=20, padx=20)
 
root.mainloop()