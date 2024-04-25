import sys
from .mainframe import MainFrame
from .settings import Settings
from .window import Window
from .map import Map

class View:
    def __init__(self):
        self.window = Window()

        self.is_fullscreen = not ("-w" in sys.argv) # Start in fullscreen?
        self.window.bind("<F11>", self.toggle_fullscreen) # Bind F11 key to toggle fullscreen
        self.window.bind("<Escape>", self.exit_fullscreen) # Bind esc key to exit fullscreen

        self.frames = {}
        
        self.add_frame("mainframe", MainFrame)
        # self.add_frame("settings", Settings)
        # self.add_frame("map", Map)
    
    def add_frame(self, name: str, Frame):
        self.frames[name] = Frame(self.window)
        self.frames[name].grid(row=0, column=0, sticky="nsew")
        
    def change_frame(self, name: str):
        self.frames[name].tkraise()
    
    def start_gui(self):
        if self.is_fullscreen: # If no -w in args, then go fullscreen 100ms after program starts
            self.window.after(100, lambda: self.window.attributes("-fullscreen", self.is_fullscreen))
        self.window.mainloop()

    def toggle_fullscreen(self, event=None):
        self.is_fullscreen = not self.is_fullscreen # Toggle
        self.window.attributes("-fullscreen", self.is_fullscreen)
        return "break" # End event

    def exit_fullscreen(self, event=None):
        self.is_fullscreen = False
        self.window.attributes("-fullscreen", False)
        return "break" # End event