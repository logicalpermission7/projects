'''
This program will create a small GUI window
'''

import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

def addApp():
    filename = filedialog.askopenfile(initialdir="/", title="Select File",
                                      filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame1, text=app, bg="gray")
        label.pack()


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame1 = tk.Frame(root, bg="white")
frame1.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

openFile =tk.Button(root, text="Open File", padx=10, pady=5, fg="#263D42", bg="#263D42", command=addApp)
openFile.pack()

runApps =tk.Button(root, text="Run Apps", padx=10, pady=5, fg="#263D42", bg="#263D42")
runApps.pack()



root.mainloop()

