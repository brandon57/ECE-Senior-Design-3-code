import tkinter as tk

class Settings(tk.Frame):
    def __init__(self, parent, controller): #This part sets up the Settings page
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="test").place(x=300, y=100)