import customtkinter as ctk

# This creates the base window of the whole program
class Window(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        self.title("ECE Senior Design 3")
        self.geometry("800x480") #Screen resolution of our 5" displays
        # self.attributes('-zoomed', True)
        # self.resizable(height=False, width=False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")
