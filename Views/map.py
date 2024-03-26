import tkinter as tk
from tkinter import Button
# import tkintermapview

class Map(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # map_widget = tkintermapview.TkinterMapView(self, )
        # self.Lat_label = tk.Label(self, text="Latitude:")
        
        # Buttons
        self.main_button = Button(self, text="Coords")
        self.main_button.grid(column=0, row=1, sticky="es")