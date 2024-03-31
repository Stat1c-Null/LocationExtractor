import tkinter as tk
from tkinter import messagebox
import time
import urllib.request
import json

#Create window
root = tk.Tk()
root.geometry("600x400")#Resolution
root.title("Ip Location Extractor")#App Title
root.configure(bg="#18122B")#Background color

def on_closing():
  if messagebox.askyesno(title="Quit?", message="Are you sure you wanna quit now ?"):
    root.destroy()

def ip_extractor():
  ip = ip_input.get()
  req = urllib.request.urlopen("http://www.ip-api.com/json/" + ip + "?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query").read()
  read_req = json.loads(req)#Extract data from json file
  offset = 10
  for key, value in read_req.items():
    tk.Label(root, text = f"{key}:{value}").grid(row=5 + offset, column = 15)
    offset += 10

#Texts
tk.Label(root, text="Location Extractor", font=('Comic Sans MS', 12), background="#BFACE2", foreground="#18122B", borderwidth=5).grid(row=0, column=4)

#Ip Label
tk.Label(root, text="Enter IP").grid(row=3, column=3)

#Ip input field
ip_input = tk.Entry(root)
ip_input.grid(row=3, column=4)

#Submit Button
submitBtn = tk.Button(root, text="Submit", bd="5", command=ip_extractor)
submitBtn.grid(row = 5, column=4)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()