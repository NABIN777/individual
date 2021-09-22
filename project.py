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


window.mainloop()