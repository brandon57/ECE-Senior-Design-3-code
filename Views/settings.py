import tkinter as tk
from tkinter import Button
import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

class Settings(ctk.CTkFrame):
    def __init__(self, *args, **kwargs): #This part sets up the Settings page
        super().__init__(*args, **kwargs)
        self.configure(corner_radius=0)
        self.configure(bg_color="white")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.toggle_fullscreen_button = ctk.CTkButton(self, text="Toggle\nFullscreen", width=125, height=50, font=("default_font", 14))
        self.toggle_fullscreen_button.grid(row=0, column=1, sticky="ne", padx=20, pady=20)
        
        self.back_button = ctk.CTkButton(self, text="Back", width=125, height=50, font=("default_font", 16))
        self.back_button.grid(row=1, column=0, sticky="sw", padx=20, pady=20)

        self.map_button = ctk.CTkButton(self, text="Map View", width=125, height=50, font=("default_font", 16))
        self.map_button.grid(row=1, column=1, sticky="se", padx=20, pady=20)