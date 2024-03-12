import tkinter as tk

# This creates the base window of the whole program
class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("ECE Senior Design 2")
        self.geometry("500x400")
        # self.attributes('-zoomed', True)
        self.resizable(height=False, width=False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0,)