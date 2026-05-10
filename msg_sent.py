

import pywhatkit
from datetime import datetime ,timedelta
import time
import tkinter as tk
from tkinter import messagebox , ttk

 #PAGE SWITCH 
def show_bot_page():
    welcome_page.pack_forget()
    next_page1.pack(fill="both", expand=True)

def show_listbox():
    list_window= tk.Toplevel(root)
    list_window.title("contact list")
    list_window.geometry("400x300")
    list_window.configure(bg="#000000")
    tk.Label(list_window, text="Saved Contact Numbers", font=("Arial", 14, "bold"),
              bg="#000000", fg="#048a18").pack(pady=10)
    listbox = tk.Listbox(list_window, font=("Arial", 12), width=40, height=10) 
    listbox.pack(pady=10)


root = tk.Tk()
root.title("WhatsApp Bot System")
root.geometry("700x400")
root.configure(bg="#000000")

welcome_page = tk.Frame(root, bg="#000000")
next_page1 = tk.Frame(root, bg="#000000")





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

contact_entry = tk.Entry(next_page1, font=("Arial", 14), width=30)
contact_entry.pack(pady=10)

tk.Button(next_page1, text ="save ",font=("Arial", 12), bg="#056410", fg="white", 
          command=lambda: messagebox.showinfo("Saved", "Contact number saved successfully!")).pack(pady=10)
tk.Button(next_page1, text= "Show list", font=("Arial", 12), bg="#056410", fg="white",
            command=lambda:show_listbox).pack(pady=10)





#  RUN 
root.mainloop()