import pywhatkit
from datetime import datetime ,timedelta
import time
import tkinter as tk
from tkinter import messagebox , ttk



Contact_number=[]


#for dashboard
def dashboard():
    root = tk.Tk()
    root.title("Whatsapp Bot System")
    root.geometry("700x400")
    root.configure(bg="#07a61f")

    lable= tk.Label(root,text=  " Welcome To Whatsapp Bot System",
                    font=("Arial",20,"bold"),bg="#07a61f",fg="white")
    lable.pack(pady=20)
    lable2=tk.Label(root,text="🖂",font=("Arial",50,"bold"),bg="#07a61f",fg="white")
    lable2.pack(pady=30)

    root.mainloop()

dashboard()