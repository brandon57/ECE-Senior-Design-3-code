from .mainframe import MainFrame
from .settings import Settings
from .window import Window
from .map import Map

class View:
    def __init__(self):
        self.window = Window()
        self.frames = {}
        
        self.add_frame("mainframe", MainFrame)
        self.add_frame("settings", Settings)
        self.add_frame("map", Map)
    
    def add_frame(self, name: str, Frame):
        self.frames[name] = Frame(self.window)
        self.frames[name].grid(row=0, column=0, sticky="nsew")
        
    def change_frame(self, name: str):
        self.frames[name].tkraise()
    
    def start_gui(self):
        self.window.mainloop()