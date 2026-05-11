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


# Save contact information
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


#  Listbox for saved contacts
def listbox():
    next_page1.pack_forget()
    next_page2.pack(fill="both", expand=True)

    listbox.delete(0, tk.END)

    for i, contact in enumerate(Contact_number):
        listbox.insert(tk.END, f"{Contact_name[i]} : {contact}")



#  MAIN PAGE

root = tk.Tk()
root.title("WhatsApp Bot System")
root.geometry("700x700")
root.configure(bg="#000000")

welcome_page = tk.Frame(root, bg="#000000")
next_page1 = tk.Frame(root, bg="#000000")
next_page2 = tk.Frame(root, bg="#000000")
next_page3 = tk.Frame(root, bg="#000000")





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

name_placeholder = "Enter contact name"
contact_entry_name.insert(0, name_placeholder)

def on_entry_click(event):
    if contact_entry_name.get()== name_placeholder:
        contact_entry_name.delete(0, tk.END)
        contact_entry_name.config(fg="black")

def on_focusout(event):
    if contact_entry_name.get()== "":
        contact_entry_name.insert(0, name_placeholder)
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

number_placeholder = "Enter contact number"
contact_entry.insert(0, number_placeholder)

def on_entry_click(event):
    if contact_entry.get()== number_placeholder:
        contact_entry.delete(0, tk.END)
        contact_entry.config(fg="black")

def on_focusout(event):
    if contact_entry.get()== "":
        contact_entry.insert(0, number_placeholder)
        contact_entry.config(fg="gray")

contact_entry.bind("<FocusIn>", on_entry_click)
contact_entry.bind("<FocusOut>", on_focusout)


tk.Button(next_page1, text ="save ",font=("Arial", 12), bg="#056410", fg="white", 
          command=show_saved_contacts).pack(pady=10)
tk.Button(next_page1, text= "Show list", font=("Arial", 12), bg="#056410", fg="white",
            command=listbox ).pack(pady=10)

tk.Button(next_page1, text="Back", font=("Arial", 12), bg="#056410", fg="white",
          command=lambda: [next_page1.pack_forget(),
                            welcome_page.pack(fill="both", expand=True)]).pack(pady=10)


#page 3

tk.Label(next_page2, text="saved contact number", font=("Arial", 14, "bold"), bg="#000000",
          fg="#048a18").pack(pady=20)

listbox = tk.Listbox(next_page2, font=("Arial", 12), width=30, height=10,selectmode="single",
                      bg="#EDE5E5", fg="#048a18", highlightbackground="#048a18", highlightcolor="#048a18"
                      , highlightthickness=2)
listbox.pack(pady=10)


#for selecting contact from listbox
def on_select(event):
    selected_index= listbox.curselection()
    if selected_index:
        selected_contact = listbox.get(selected_index)

        next_page2.pack_forget()
        next_page3.pack(fill="both", expand=True)

        
listbox.bind("<<ListboxSelect>>", on_select)



tk.Button(next_page2, text="Back", font=("Arial", 12), bg="#056410", fg="white",
          command=lambda: [next_page2.pack_forget(),
                           next_page1.pack(fill="both", expand=True)]).pack(pady=10)


#page 4
tk.Label(next_page3, text="Write your Message", font=("Arial", 14, "bold"), bg="#000000",
          fg="#048a18").pack(pady=20)
entry_message = tk.Entry(next_page3, font=("Arial", 12), width=40, fg="Black")
entry_message.pack(pady=10)


# Send message function
def send_message():
    selected_index= listbox.curselection() # Get the selected index from the listbox
    if selected_index:
        selected_index = selected_index[0] # Get the first selected index
        selected_contact = Contact_number[selected_index]
        message = entry_message.get()
        if message:
            pywhatkit.sendwhatmsg_instantly(
                selected_contact,
                message,
                wait_time=20,
                tab_close=True
            )
            messagebox.showinfo("Success", "Message sent successfully!")
        else:
            messagebox.showwarning("Input Error", "Please enter a message to send.")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact from the list.")



tk.Button(next_page3, text="Send Message", font=("Arial", 12), bg="#056410", fg="white", command=send_message).pack(pady=10)

    
tk.Button(next_page3, text="Back", font=("Arial", 12), bg="#056410", fg="white",     
            command=lambda: [next_page3.pack_forget(),
                             next_page2.pack(fill="both", expand=True)]).pack(pady=10)
                                
    

#  RUN 
root.mainloop()