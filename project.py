'''creating password manager'''
from tkinter import *
from tkinter import messagebox
import json
import pyperclip
from password import password_generator


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="Orange")


def get_password():
    password = password_generator()
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(END, password)



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


window.mainloop()