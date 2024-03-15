import tkinter as tk
from tkinter import Button

class Settings(tk.Frame):
    def __init__(self, *args, **kwargs): #This part sets up the Settings page
        tk.Frame.__init__(self, *args, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)