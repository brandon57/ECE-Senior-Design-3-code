import customtkinter as ctk
import tkintermapview

class Map(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        ctk.CTkFrame.__init__(self, *args, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        self.map_widget = tkintermapview.TkinterMapView(self)
        # self.map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.map_widget.grid(column=0, row=0, sticky="wn")
        # self.Lat_label = tk.Label(self, text="Latitude:")
        # self.map_widget.set_position()
        
        # Buttons
        self.main_button = ctk.CTkButton(self, text="Coords")
        self.main_button.grid(column=0, row=1, sticky="es")