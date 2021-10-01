

from tkinter import *
from tkhtmlview import HTMLLabel
 
# Create Object
root = Tk()
 
# Set Geometry
root.geometry("400x400")
 
# Add label
my_label = HTMLLabel(root, html="""
<li> LINK FOR FACEBOOK</LI>
    <ul>
        <li><a href='https://www.facebook.com//'>Facebook</a></li>
       
    </ul>
    """)
 
my_label.pack(pady=20, padx=20)
 
root.mainloop()