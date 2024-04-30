from Views.numericentry import NumericEntry
from Controllers.numericentry import NumericEntryController
from threading import *
from IO.COMS import *
from IO.GPS_I2C import getCoords
import tkintermapview
import time

"""This is the controller for the MainFrame Object""" 

class MainFrame_Controller():
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.frame = self.view.frames["mainframe"]
        self.on = False
        self.map = False
        self.set_mode(self.model.get_mode())    # Sets the mode to what it was before
        self.marker2 = self.frame.map_widget.set_marker(0, 0, marker_color_outside="darkgray", marker_color_circle="gray")
        self.marker = self.frame.map_widget.set_marker(0, 0)

        self.lastlat = 0
        self.lastlong = 0
        self.latestCoords = []

        self.configure()
        
        self.GPS = None
        self.stop_thread = Event()
        self.stop_second_thread = Event()
    
    def configure(self): # Configures the buttons
        
        self.frame.stop_button.configure(command=self.start)
        self.frame.change_mode_button.configure(command= lambda: self.set_mode(~self.model.get_mode()))
        self.frame.use_current_button.configure(command= lambda: Thread(target= self.use_current_coords, daemon=True).start())
        self.frame.map_button.configure(command= self.show_map)
        self.frame.base_latitude_button.configure(command=lambda: self.showNumericEntry('latitude'), text= f"{self.model.get_coords()[0]:.8f}")
        self.frame.base_longitude_button.configure(command=lambda: self.showNumericEntry('longitude'), text= f"{self.model.get_coords()[1]:.8f}")

        self.frame.map_widget.canvas.unbind("<ButtonPress-1>")
        self.frame.map_widget.canvas.unbind("<B1-Motion>")
        self.frame.map_widget.set_zoom(19)
    
    def start(self):
            
        if self.stop_thread:
            self.stop_thread.clear()
        if self.stop_second_thread:
            self.stop_second_thread.clear()
        self.on = not self.on
        
        if self.on == False:
            self.frame.stop_button.configure(text="Start", fg_color="green")
            self.frame.change_mode_button.lift()
            if self.map:
                self.frame.map_group.lift()
                self.frame.stop_button.lift()
                self.frame.map_button.lift()
            time.sleep(0.1) # Not my favorite fix but sometimes the base thread still writes awaiting location if it didnt finish
            if self.frame.received_location_value.cget('text') == "Awaiting data" or self.frame.received_location_value.cget('text') == "Acquiring location":
                self.frame.received_location_value.configure(text= "")
                self.frame.calculated_differential_value.configure(text= "")
                self.frame.actual_location_value.configure(text= "")
            self.frame.receiver_value.configure(text= "")
            self.stop()
        else:
            self.frame.stop_button.configure(text="STOP", fg_color="darkred")
            self.frame.change_mode_button.lower()
            
            if self.model.get_mode() != 0:
                self.GPS = Thread(target= lambda: self.Base(), daemon=True)
            else:
                self.GPS = Thread(target= lambda: self.Mobile(), daemon=True)

            
            self.CoordsSrv = Thread(target= lambda: self.CoordsService(), daemon=True)
            self.CoordsSrv.start()
            self.GPS.start()

    
    def Base(self):
        last_coords = []
        last_transmission = time.time_ns()
        while not self.stop_thread.is_set():
            last_tx_ago = time.time_ns() - last_transmission
            coords = self.latestCoords # grabs coordinates
            if coords != []:
                if (last_coords != coords or last_tx_ago > 1000000000): # did the coords change or has it been a full second since last send?
                    last_coords = coords
                    if (last_tx_ago > 500000000): # was it over a 1/2 sec ago the last one was sent?
                        last_transmission = time.time_ns()
                        user_coords = self.model.get_coords()
                        try:
                            lat_diff = (user_coords[0] - coords[0])
                            longit_diff = (user_coords[1] - coords[1])
                            if not self.stop_thread.is_set():
                                if self.map == False:
                                    self.frame.received_location_value.configure(text= f"{coords[0]:.8f}, {coords[1]:.8f}")
                                    self.frame.calculated_differential_value.configure(text= f"{lat_diff:.8f}, {longit_diff:.8f}")
                                    self.frame.actual_location_value.configure(text= f"{self.model.get_coords()[0]:.8f}, {self.model.get_coords()[1]:.8f}")
                                else:
                                    self.marker2.set_position(coords[0], coords[1])
                                    time.sleep(0.01)
                                    self.marker.set_position(user_coords[0], user_coords[1])
                                    self.marker.set_text(str(round(user_coords[0], 8)) + ", " + str(round(user_coords[1], 8)))                          
                                print(coords) #Testing
                                sendData(f"{lat_diff:.8f},{longit_diff:.8f}")
                        except:
                            print("Couldn't set current text")
                            continue
            else:
                self.frame.received_location_value.configure(text= "Acquiring location")
                self.frame.calculated_differential_value.configure(text= "Acquiring location")
                self.frame.actual_location_value.configure(text= "Acquiring location")
            time.sleep(0.05)
    
    def Mobile(self):
        self.frame.receiver_value.configure(text= "Awaiting data")
        self.frame.received_location_value.configure(text= "Awaiting data")
        self.frame.calculated_differential_value.configure(text= "Awaiting data")
        self.frame.actual_location_value.configure(text= "Awaiting data")
        while not self.stop_thread.is_set():
            rx = receiveData()
            if rx != 'error':
                data = rx.split(",")
                print(data) #Testing
                coords = self.latestCoords
                try:
                    lat = coords[0] + float(data[2])
                    longit = coords[1] + float(data[3])
                    if not self.stop_thread.is_set():
                        if self.map == True:
                            self.marker2.set_position(coords[0], coords[1])
                            time.sleep(0.01)
                            self.marker.set_position(lat, longit)
                            self.marker.set_text(f"{lat:.8f}, {longit:.8f}")
                            
                            if abs(lat - self.lastlat) > 0.0004 or abs(longit - self.lastlong) > 0.0002:
                                self.frame.map_widget.set_position(lat, longit)
                                self.lastlat = lat
                                self.lastlong = longit
                        else:
                            self.frame.receiver_value.configure(text=data[4] + " RSSI")
                            self.frame.received_location_value.configure(text= f"{coords[0]:.8f}, {coords[1]:.8f}")
                            self.frame.calculated_differential_value.configure(text= data[2] + "," + data[3])
                            self.frame.actual_location_value.configure(text= f"{lat:.8f}, {longit:.8f}")
                except:
                    print("Couldn't set current text")
                    continue
        
    
    def CoordsService(self):
        print("Begin CoordsService")
        while not self.stop_second_thread.is_set():
            try:
                coords = getCoords()
                if not self.stop_second_thread.is_set():
                    self.latestCoords = coords
            except:
                print("getCoords failed") 
                time.sleep(1)
        print("End CoordsService")

    
    def set_mode(self, mode):
        self.model.set_mode(mode)
        if mode == 0:
            self.frame.mode_label.configure(text="This device is in mobile receiver mode")
            self.frame.base_location_group.lower()
            self.frame.receiver_group.lift()
        else:
            self.frame.mode_label.configure(text="This device is in base station mode")
            self.frame.receiver_group.lower()
            self.frame.base_location_group.lift()
    
    def show_map(self):
        self.map = not self.map
        if self.map == False:
            self.frame.map_button.configure(text="Map View")
            self.frame.map_group.lower()
        else:
            if self.model.get_mode() != 0:
                coords = self.model.get_coords()
                self.frame.map_widget.set_position(round(coords[0], 8), round(coords[1], 8))
            self.frame.map_button.configure(text="Stats View")
            self.frame.map_group.lift()
            self.frame.stop_button.lift()
            self.frame.map_button.lift()
            
    def use_current_coords(self):
        if self.frame.base_latitude_button.cget('text') != "Acquiring location" or self.frame.base_longitude_button.cget('text') != "Acquiring location":
            if not self.on:
                self.frame.base_latitude_button.configure(text= "Acquiring location")
                self.frame.base_longitude_button.configure(text= "Acquiring location")
                self.frame.stop_button.lower()
                self.frame.map_button.lower()
                coords = getCoords()
                newlat = coords[0]
                newlong = coords[1]
                if self.frame.base_latitude_button.cget('text') != "Acquiring location" or self.frame.base_longitude_button.cget('text') != "Acquiring location":
                    self.frame.stop_button.lift()
                    self.frame.map_button.lift()
                    return
            else:
                raw_value = self.frame.received_location_value.cget('text')
                parts = raw_value.split(", ")
                try:
                    newlat = float(parts[0])
                    newlong = float(parts[1])
                except:
                    print("Failed to read text box value")
                
            try:
                self.model.update_lat(f"{newlat:.8f}")
                self.model.update_longit(f"{newlong:.8f}")
                self.frame.base_latitude_button.configure(text= f"{newlat:.8f}")
                self.frame.base_longitude_button.configure(text= f"{newlong:.8f}")
                self.frame.stop_button.lift()
                self.frame.map_button.lift()
                return
            except:
                print("Couldn't set current text")
        
    def showNumericEntry(self, input_type):
        self.numeric_entry_controller = NumericEntryController(self.frame, self.model, input_type, self)
        self.numeric_entry_controller.view.grid(row=0, column=0, rowspan=4, columnspan=6, padx=0, pady=0, sticky="nsew")
        
    def stop(self):
        self.stop_second_thread.set()
        self.stop_thread.set()
        # if self.GPS.is_alive():
        #     self.GPS.join()
        if self.CoordsSrv.is_alive():
            self.CoordsSrv.join()
        self.GPS = None
        self.CoordsSrv = None
        self.latestCoords.clear()
