import tkinter as tk
from tkinter import ttk, Button
import tkintermapview

class MainFrame(tk.Frame):
    def __init__(self, *args, **kwargs): #This part sets up the GUI
        tk.Frame.__init__(self, *args, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # Labels
        self.latNum_text, self.longNum_text = tk.StringVar(), tk.StringVar()
        self.Lat_label = tk.Label(self, text="Latitude:")
        self.latNum = tk.Label(self, textvariable=self.latNum_text)
        self.long_label = tk.Label(self, text="Longitude:")
        self.longNum = tk.Label(self, textvariable=self.longNum_text)
        self.Lat_label.grid(column=1, row=1, sticky="ew")
        # self.Lat_label.place(x=100, y=100)
        self.latNum.grid(column=2, row=1, padx=10, sticky="ew")
        # self.latNum.place(x=180, y=100)
        self.long_label.grid(column=4, row=1, sticky="ew")
        # self.long_label.place(x=300, y=100)
        self.longNum.grid(column=5, row=1, padx=10, sticky="ew")
        # self.longNum.place(x=380, y=100)
        self.latNum_text.set("0.0")
        self.longNum_text.set("0.0")
        
        # Buttons
        self.modeButton_text, self.startButton_text, self.settingsButton_text, self.map_button_text = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
        self.start_button = Button(self, textvariable=self.startButton_text)
        self.start_button.grid(column=3, row=2, sticky="ew")
        # self.start_button.place(x=220, y=160)
        self.startButton_text.set("Start")
        
        self.modeButton = Button(self, textvariable=self.modeButton_text)
        self.modeButton.grid(column=0, row=3, sticky="sw")
        # self.modeButton.place(x=0, y=370)
        self.modeButton_text.set("Receiver")
        
        self.map_button = Button(self, textvariable=self.map_button_text)
        self.map_button.grid(column=6, row=3, sticky="es")
        self.map_button_text.set("Map")
        
        self.settings_button = Button(self, text="Settings")
        self.settings_button.grid(column=6, row=0, sticky="ne")
        
        # Map
        self.map_widget = tkintermapview.TkinterMapView(self)