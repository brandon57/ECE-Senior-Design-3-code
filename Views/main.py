# from typing import TypedDict

from .display import MainPage
from .settings import Settings
from .window import Window

class View:
    def __init__(self):
        self.window = Window()
        self.frames = {}
        
        self.add_frame("mainpage", MainPage)
        #self.add_frame("settings", Settings)
    
    def add_frame(self, name: str, Frame):
        self.frames[name] = Frame(self.window)
        #self.frames[name].place(1234)
        
    def change_frame(self, name: str):
        self.frames[name].tkraise()
    
    def start_gui(self):
        self.window.mainloop()