import tkinter as tk
from tkinter import messagebox
import time

#Create window
root = tk.Tk()
root.geometry("500x300")#Resolution
root.title("Ip Location Extractor")#App Title
root.configure(bg="#18122B")#Background color

def on_closing():
  if messagebox.askyesno(title="Quit?", message="Are you sure you wanna quit now ?"):
    root.destroy()

#Texts
tk.Label(root, text="Location Extractor", font=('Comic Sans MS', 12), background="#BFACE2", foreground="#18122B", borderwidth=5).grid(row=0, column=2)
#title.pack(pady=15)

tk.Label(foreground="#18122B").grid(row=1)
tk.Label(root, text="Enter IP").grid(row=2)

ip_input = tk.Entry(root)

ip_input.grid(row=2, column=1)


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()