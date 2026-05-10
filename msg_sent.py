import pywhatkit
from datetime import datetime ,timedelta
import time
import tkinter as tk
from tkinter import messagebox , ttk



Contact_number = []
Contact_name= []


 #PAGE SWITCH 
def show_bot_page():
    welcome_page.pack_forget()
    next_page2.pack_forget()
    next_page1.pack(fill="both", expand=True)


def show_saved_contacts():
    name = contact_entry_name.get()
    number = contact_entry.get()
    if name and number:
        Contact_name.append(name)
        Contact_number.append(number)
        messagebox.showinfo("Saved", " Your Contact has been saved successfully!")
        contact_entry.delete(0, tk.END)
        contact_entry_name.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both contact name and number.")



def listbox():
    next_page1.pack_forget()
    next_page2.pack(fill="both", expand=True)
    listbox = tk.Listbox(next_page2, font=("Arial", 12), width=30, height=10)
    listbox.pack(pady=10)
    for i, contact in enumerate(Contact_number):
        listbox.insert(tk.END, f"{Contact_name[i]}: {contact}")




root = tk.Tk()
root.title("WhatsApp Bot System")
root.geometry("700x400")
root.configure(bg="#000000")

welcome_page = tk.Frame(root, bg="#000000")
next_page1 = tk.Frame(root, bg="#000000")
next_page2 = tk.Frame(root, bg="#000000")





#  Welcome Page 1
welcome_page.pack(fill="both", expand=True)

tk.Label(
    welcome_page,
    text="Welcome To WhatsApp Bot System",
    font=("Arial", 20, "bold"),
    bg="#000000",
    fg="#048a18"
).pack(pady=20)

tk.Label(
    welcome_page,
    text="🖂",
    font=("Arial", 50),
    bg="#000000",
    fg="#048a18"
).pack(pady=30)

tk.Button(
    welcome_page,
    text="Next",
    command=show_bot_page,
    font=("Arial", 14, "bold"),
    bg="#056410",
    fg="white"
).pack(pady=20)


#  PAGE 2 

tk.Label(
    next_page1,
    text="Enter Contact Name",
    font=("Arial", 14, "bold"),
    bg="#000000",
    fg="#048a18"
).pack(pady=20)

contact_entry_name = tk.Entry(next_page1,font=("Arial", 14), width=30 ,fg="gray")
contact_entry_name.pack(pady=10)

# placeholder for contact name entry
placeholder_text = "Enter contact name"
contact_entry_name.insert(0, placeholder_text)

def on_entry_click(event):
    if contact_entry_name.get()== placeholder_text:
        contact_entry_name.delete(0, tk.END)
        contact_entry_name.config(fg="black")

def on_focusout(event):
    if contact_entry_name.get()== "":
        contact_entry_name.insert(0, placeholder_text)
        contact_entry_name.config(fg="gray")

contact_entry_name.bind("<FocusIn>", on_entry_click)
contact_entry_name.bind("<FocusOut>", on_focusout)



tk.Label(
    next_page1,
    text="Enter Contact Number",
    font=("Arial", 14, "bold"),
    bg="#000000",
    fg="#048a18"
).pack(pady=20)

tk.Label(
    next_page1,
    text="(Include country code, e.g., +880 for Bangladesh)",
    font=("Arial", 10),
    bg="#000000",
    fg="#048a18"
).pack(pady=5)


# placeholder for contact number entry
contact_entry = tk.Entry(next_page1, font=("Arial", 14), width=30, fg="gray")
contact_entry.pack(pady=10)

placeholder_text = "Enter contact number"
contact_entry.insert(0, placeholder_text)

def on_entry_click(event):
    if contact_entry.get()== placeholder_text:
        contact_entry.delete(0, tk.END)
        contact_entry.config(fg="black")

def on_focusout(event):
    if contact_entry.get()== "":
        contact_entry.insert(0, placeholder_text)
        contact_entry.config(fg="gray")

contact_entry.bind("<FocusIn>", on_entry_click)
contact_entry.bind("<FocusOut>", on_focusout)


tk.Button(next_page1, text ="save ",font=("Arial", 12), bg="#056410", fg="white", 
          command=show_saved_contacts).pack(pady=10)
tk.Button(next_page1, text= "Show list", font=("Arial", 12), bg="#056410", fg="white",
            command=listbox ).pack(pady=10)



#page 3
tk.Label(next_page2, text="saved contact number", font=("Arial", 14, "bold"), bg="#000000", fg="#048a18").pack(pady=20)










#  RUN 
root.mainloop()