from tkinter import*
from tkcalendar import DateEntry
from tkinter import messagebox
root = Tk()
root.maxsize(500,500)
root.minsize(500,500)
root.configure(background='peru')
def msg():
    select=var.get()
    if select==0:
        response=messagebox.showwarning("FAILED","PLEASE FILL ALL CONTENT")
    elif (entry_2.index("end") == 0):
        messagebox.askyesno('Missing E-mail', 'you sure wanna miss it?')
    else:
      response = messagebox.showinfo("Thank you", "YOUR REGISTER IS DONE")




root.title("Registration Form")
label_0 = Label(root, text="Registration form",borderwidth=4,relief=GROOVE,width=20,font=("bold", 20),bg="green",fg="white")
label_0.place(x=90,y=53)
label_1 = Label(root, text="FullName:",width=20,borderwidth=4,relief=GROOVE,font=("bold", 10),bg="peru")
label_1.place(x=50,y=130)
entry_1 = Entry(root,fg="green")
entry_1.place(x=240,y=130)
label_2 = Label(root, text="Email:",borderwidth=4,relief=GROOVE,width=20,font=("bold", 10),bg="peru")
label_2.place(x=50,y=180)
entry_2 = Entry(root)
entry_2.place(x=240,y=180)
label_3 = Label(root, text="Gender:",borderwidth=4,relief=GROOVE,width=20,font=("bold", 10),bg="peru")
label_3.place(x=50,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1,bg="orange").place(x=235,y=230)
Radiobutton(root, text="Female",padx = 5, variable=var, value=2,bg="orange").place(x=290,y=230)
Radiobutton(root,text="other",padx=5,variable=var,  value=3,bg="orange").place(x=355,y=230)
label_4 = Label(root, text="Age:",borderwidth=4,relief=GROOVE,width=20,font=("bold", 10),bg="peru")
label_4.place(x=50,y=280)
entry_2 = Entry(root)
entry_2.place(x=240,y=280)
l4 = Label(root,borderwidth=4,relief=GROOVE, text="DOB:",width=20,font=("bold",10),bg='peru')
l4.place(x=50,y=330)

dob = DateEntry(root, width=27, background='brown', foreground='white',date_pattern='dd/mm/Y', borderwidth=3)
dob.place(x=240,y=330)
f1=Frame(root,bg="RED",borderwidth=6,relief=GROOVE)
f1.pack(side=BOTTOM)
btn=Button(f1, text='Submit',width=20,bg='BLUE',fg='white',command=msg)
btn.pack()
s=Label(text="©Nirajan,NEPAL",font=("italic",10))
s.place(x=395 ,y=480)
root.mainloop()