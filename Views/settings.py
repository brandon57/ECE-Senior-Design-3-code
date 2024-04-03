import tkinter as tk
from tkinter import Button

class Settings(tk.Frame):
    def __init__(self, *args, **kwargs): #This part sets up the Settings page
        tk.Frame.__init__(self, *args, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.toggle_fullscreen_button = tk.Button(self, text="Toggle Fullscreen")
        self.toggle_fullscreen_button.grid(row=0, column=1, sticky="ne", padx=10, pady=10)

        self.back_button = tk.Button(self, text="Back")
        self.back_button.grid(row=1, column=0, sticky="sw", padx=10, pady=10)