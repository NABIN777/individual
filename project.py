'''creating password manager'''
from tkinter import *
from tkinter import messagebox
import json
import pyperclip
from password import password_generator
from PIL import Image,ImageTk
import subprocess


window = Tk()
window.title("Password Manager")
window.config(bg="#111d5e")
window.resizable(FALSE, FALSE)
window.geometry('850x500')
window.wm_iconbitmap("lock.ico")


# generates randoms sting,integers and special charecter
def get_password():
    password = password_generator()
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(END, password)


# json file handling
def database_manager(new_user_entry):
    try:

        with open("data.json", mode="r") as old_password_file:
            # reading old password data
            password_data = json.load(old_password_file)

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open("data.json", mode="w") as new_password_file:
            json.dump(new_user_entry, new_password_file, indent=4)
    # if there is old password data,
    else:
        #  New user entry json data will be updated to the old passwords data
        password_data.update(new_user_entry)
        # Writing either the updated password data or the new user entry json data
        with open("data.json", mode="w") as old_password_file:
            json.dump(password_data, old_password_file, indent=4)
    finally:
      
        website_entry.delete(0, END)
        password_entry.delete(0, END)


        
def save_password():
    # getting user entry data
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # Dialog to user to make sure password is correct
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title="Confirm entries", message=f"These are the details you entered\n"
                                                                        f"Email: {email}"
                                                                        f"\nPassword: {password}\nIs it okay to save ?")
        if is_ok:
            # copying password to our clipboard
            pyperclip.copy(password)
            # new user data to be entered into current password data file as json
            new_entry_in_json = {
                website:
                    {
                        "Email": email,
                        "Password": password
                    }
            }
            # Writing to the password database or updating it
            database_manager(new_entry_in_json)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_password():
    # Getting user website entry
    website = website_entry.get()
    # for error handling
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please enter a website to search")
    else:
       
        try:
           
            with open("data.json", mode="r") as old_password_file:
                # reading old password data
                password_data = json.load(old_password_file)
       
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            messagebox.showinfo(title="No passwords saved", message="Sorry, you have not saved any password before")
        else:
           
            if website in password_data:
                email = password_data[website]["Email"]
                password = password_data[website]["Password"]
                # Save to clipboard message box
                is_clipboard = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {password}"
                                                                             f"\n\nSave to clipboard ?")
               
                if is_clipboard:
                    # save password to clipboard
                    pyperclip.copy(password)
                    messagebox.showinfo(title="Saved to clipboard", message="Password has been saved to clipboard")
            
                messagebox.showinfo(title="Password not saved for this website", message=f"The password for {website}\n"
                                                                                         f"has not been saved")

# adding images and canvas
l_1=Image.open("logo.png")
l_1=l_1.resize((300,255),Image.ANTIALIAS)
l_1=ImageTk.PhotoImage(l_1)
canvas = Canvas(width=200, height=200, bg="ORANGE", highlightthickness=0)
canvas.config()
canvas.create_image(100, 100, image=l_1)
canvas.place(x=325,y=10)

# helps to add images 
image_1=Image.open("search.png")
image_1=image_1.resize((190,22),Image.ANTIALIAS)
image_1=ImageTk.PhotoImage(image_1)


image_2=Image.open("Generate.png")
image_2=image_2.resize((190,22),Image.ANTIALIAS)
image_2=ImageTk.PhotoImage(image_2)

image_3=Image.open("add.png")
image_3=image_3.resize((200,20),Image.ANTIALIAS)
image_3=ImageTk.PhotoImage(image_3)

# functions for hyperlink window button

# subprocess the page facebook.py
def run_facebook():
    window.destroy() #destroy current window
    subprocess.call(["python","facebook.py"])


# subprocess the page google.py
def run_google():
    window.destroy()
    subprocess.call(["python","google.py"])



# subprocess the page youtube.py
def run_youtube():
    window.destroy()
    subprocess.call(["python","youtube.py"]) #giving name of file which to be subprocess







# Label
# Label for Website
website_label = Label(text="Website:", bg="#111d5e", padx=20, font=("Times", 14), fg="RED")
website_label.place(x=40,y=200)

# Label for Email/Username
email_label = Label(text="Email/Username:", bg="#111d5e", padx=20, font=("Times", 14), fg="RED")
email_label.place(x=40,y=225)

# Label for Password
password_label = Label(text="Password:", bg="#111d5e", padx=20, font=("Times", 14), fg="RED")
password_label.place(x=40,y=250)

# Entry widgets
website_entry = Entry(width=30, bg="silver", fg="RED", font=("Times", 14))
website_entry.insert(END, string="")
website_entry.place(x=200,y=200)
# starting cursor focus
website_entry.focus()
email_entry = Entry(width=30, bg="silver", fg="RED", font=("Times", 14))
email_entry.insert(END, string="")
email_entry.place(x=200,y=225)
# set default email
email_entry.insert(0, "nabin.kh@example.com")

password_entry = Entry(width=30, bg="silver", fg="RED", font=("Times", 14))
password_entry.insert(END, string="")
password_entry.place(x=200,y=250)

# buttons
search_button = Button(window,command=search_password,image=image_1)
search_button.place(x=485,y=200)

generate_button = Button(window,command=get_password,image=image_2)
generate_button.place(x=485,y=245)
add_button = Button(window,command=save_password,image=image_3,width=145)
add_button.place(x=695,y=245)




# canvas 

main_frame = Frame(window,bg="black")
main_frame.place(x=0, y=278)

my_canvas = Canvas(main_frame, width=846, height=250,bg="#111d5e")
my_canvas.pack(side=LEFT, fill=BOTH)

#Labeling inside canvas

text_label=Label(my_canvas,text="© Nirajan coporate Limited",fg="silver",bg="#111d5e")
text_label.place(x=330,y=180)

text_label1=Label(my_canvas,text="Kirtipur,Kathmandu",fg="silver",bg="#111d5e")
text_label1.place(x=350,y=200)


text_label1=Label(my_canvas,text="LINKS",fg="silver",bg="#111d5e",relief=GROOVE,borderwidth=6,width=25)
text_label1.place(x=315,y=5,height=40)

# button for iside of creaed canvas

Button_f=Button(my_canvas,text="facebook",relief=GROOVE,bg="Blue",fg="white",width=15,command=run_facebook)
Button_f.place(x=2,y=48)

Button_g=Button(my_canvas,text="G Google",relief=GROOVE,bg="blue",fg="green",width=15,command=run_google)
Button_g.place(x=360,y=48)

Button_y=Button(my_canvas,text="YOUTUBE ▶️",relief=GROOVE,bg="Red",fg="white",width=15,command=run_youtube)
Button_y.place(x=730,y=48)




window.mainloop()