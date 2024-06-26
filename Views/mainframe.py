import customtkinter as ctk
import tkintermapview

class MainFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs): #This part sets up the GUI
        ctk.CTkFrame.__init__(self, *args, **kwargs)
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=3)
        self.grid_rowconfigure((0, 3), weight=0)

        font_size = 20

        # Mode
        # Mode label
        self.mode_label = ctk.CTkLabel(self, font=("default_font", font_size + 2))
        self.mode_label.grid(row=0, column=0, columnspan=6)

        self.change_mode_button = ctk.CTkButton(self, text="Change Mode", font=("default_font", font_size), width=144, height=64, hover=False)
        self.change_mode_button.grid(row=0, column=5, padx=20, pady=10, sticky="ne")
        
        # Base location frame
        self.base_location_group = ctk.CTkFrame(self, corner_radius=10)
        self.base_location_group.grid(row=1, column=0, columnspan=6, padx=60, pady=10, sticky="nsew")
        self.base_location_group.grid_rowconfigure((0, 1), weight=1)
        self.base_location_group.grid_columnconfigure((0, 1, 2), weight=1)

        self.base_latitude_label = ctk.CTkLabel(self.base_location_group, text="Set fixed latitude: ", font=("default_font", font_size), anchor='e')
        self.base_latitude_label.grid(row=0, column=0, sticky="ew")
        self.base_latitude_button = ctk.CTkButton(self.base_location_group, text="", font=("default_font", font_size), anchor='w', fg_color="white", text_color="black", corner_radius=0, hover=False)
        self.base_latitude_button.grid(row=0, column=1, sticky="ew")

        self.base_longitude_label = ctk.CTkLabel(self.base_location_group, text="Set fixed longitude: ", font=("default_font", font_size), anchor='e')
        self.base_longitude_label.grid(row=1, column=0, sticky="ew")
        self.base_longitude_button = ctk.CTkButton(self.base_location_group, text="", font=("default_font", font_size), anchor='w', fg_color="white", text_color="black", corner_radius=0, hover=False)
        self.base_longitude_button.grid(row=1, column=1, sticky="ew")

        self.use_current_button = ctk.CTkButton(self.base_location_group, text="Use Current Location", font=("default_font", font_size), width=144, height=64, hover=False)
        self.use_current_button.grid(row=0, column=2, rowspan=2, padx=10, pady=10)

        # Receiver frame
        self.receiver_group = ctk.CTkFrame(self, corner_radius=10)
        self.receiver_group.grid(row=1, column=0, columnspan=6, padx=60, pady=10, sticky="nsew")
        self.receiver_group.grid_rowconfigure((0, 1), weight=1)
        self.receiver_group.grid_columnconfigure((0, 1), weight=1)

        self.receiver_label = ctk.CTkLabel(self.receiver_group, text="LoRa Signal Strength:  ", font=("default_font", font_size), anchor='e')
        self.receiver_label.grid(row=0, column=0, rowspan=2, sticky="e")

        self.receiver_value = ctk.CTkLabel(self.receiver_group, text="", font=("default_font", font_size), anchor='w')
        self.receiver_value.grid(row=0, column=1, rowspan=2, sticky="w")

        # Stats frame
        self.stats_group = ctk.CTkFrame(self, corner_radius=10)
        self.stats_group.grid(row=2, column=0, columnspan=6, padx=60, pady=10, sticky="nsew")
        self.stats_group.grid_rowconfigure((0, 1, 2), weight=1)
        self.stats_group.grid_columnconfigure(0, weight=1)
        self.stats_group.grid_columnconfigure(1, weight=3)

        self.received_location_label = ctk.CTkLabel(self.stats_group, text="Received location: ", font=("default_font", font_size), anchor='e')
        self.received_location_label.grid(row=0, column=0, sticky="e")
        self.received_location_value = ctk.CTkLabel(self.stats_group, text="", font=("default_font", font_size), anchor='w')
        self.received_location_value.grid(row=0, column=1, sticky="w")

        self.calculated_differential_label = ctk.CTkLabel(self.stats_group, text="Calculated differential: ", font=("default_font", font_size), anchor='e')
        self.calculated_differential_label.grid(row=1, column=0, sticky="e")
        self.calculated_differential_value = ctk.CTkLabel(self.stats_group, text="", font=("default_font", font_size), anchor='w')
        self.calculated_differential_value.grid(row=1, column=1, sticky="w")

        self.actual_location_label = ctk.CTkLabel(self.stats_group, text="Actual location: ", font=("default_font", font_size), anchor='e')
        self.actual_location_label.grid(row=2, column=0, sticky="e")
        self.actual_location_value = ctk.CTkLabel(self.stats_group, text="", font=("default_font", font_size), anchor='w')
        self.actual_location_value.grid(row=2, column=1, sticky="w")

        # Map frame
        self.map_group = ctk.CTkFrame(self, corner_radius=0)
        self.map_group.grid(row=0, column=0, rowspan = 4, columnspan=6, padx=0, pady=0, sticky="nsew")
        self.map_group.lower()
        self.map_group.grid_rowconfigure(0, weight=1)
        self.map_group.grid_columnconfigure(0, weight=1)

        self.map_widget = tkintermapview.TkinterMapView(self.map_group)
        self.map_widget.grid(row=0, column=0, sticky="nsew")

        self.stop_button = ctk.CTkButton(self, text="Start", fg_color="green", font=("default_font", font_size), width=144, height=64, hover=False)
        self.stop_button.grid(row=3, column=0, padx=20, pady=20, sticky="sw")

        self.map_button = ctk.CTkButton(self, text="Map View", font=("default_font", font_size), width=144, height=64, hover=False)
        self.map_button.grid(row=3, column=5, padx=20, pady=20, sticky="se")