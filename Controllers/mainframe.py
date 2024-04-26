from Views.numericentry import NumericEntry
from Controllers.numericentry import NumericEntryController
from threading import *
from IO.COMS import *
from IO.GPS_I2C import getCoords

"""This is the controller for the MainFrame Object""" 

class MainFrame_Controller():
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.frame = self.view.frames["mainframe"]
        self.on = False
        self.map = False
        self.set_mode(self.model.get_mode())    # Sets the mode to what it was before
        
        self.configure()
        
        self.GPS = None
        self.stop_thread = Event()
    
    def configure(self): # Configures the buttons
        
        self.frame.stop_button.configure(command=self.start)
        self.frame.change_mode_button.configure(command= lambda: self.set_mode(~self.model.get_mode()))
        self.frame.use_current_button.configure(command=self.use_current_coords)
        self.frame.map_button.configure(command= self.show_map)
        self.frame.base_latitude_button.configure(command=lambda: self.showNumericEntry('latitude'), text= "  " + f"{self.model.get_coords()[0]:.8f}")
        self.frame.base_longitude_button.configure(command=lambda: self.showNumericEntry('longitude'), text= " " + f"{self.model.get_coords()[1]:.8f}")
        
        self.show_map()
    
    def start(self):
        if self.stop_thread:
            self.stop_thread.clear()
        self.on = not self.on
        
        if self.on == False:
            self.frame.stop_button.configure(text="Start", fg_color="green")
            self.frame.change_mode_button.lift()
            self.stop()
        else:
            self.frame.stop_button.configure(text="STOP", fg_color="darkred")
            self.frame.change_mode_button.lower()
            
            if self.model.get_mode() != 0:
                self.GPS = Thread(target= lambda: self.Base(), daemon=True)
            else:
                self.GPS = Thread(target= lambda: self.Mobile(), daemon=True)
    
            self.GPS.start()
    
    def Base(self):
        while not self.stop_thread.is_set():
            coords = getCoords() # grabs coordinates
            user_coords = self.model.get_coords()
            try:
                lat_diff = str(round(-(user_coords[0] - coords[0]), 8))
                longit_diff = str(round(-(user_coords[1] - coords[1], 8)))
                if not self.stop_thread.is_set():
                    if self.map == True:
                        self.frame.map_widget.set_position(round(coords[0], 8), round(coords[1], 8), marker=True)
                    else:
                        self.frame.received_location_value.configure(text= str(round(coords[0], 8)) + ", " + str(round(coords[1], 8)))
                        self.frame.calculated_differential_value.configure(text= lat_diff + ", " + longit_diff)
                        # print(coords) #Testing
                        sendData(lat_diff + "," + longit_diff)
            except:
                continue
    
    def Mobile(self):
        while not self.stop_thread.is_set():
            data = receiveData().split(",")
            print(data) #Testing
            coords = getCoords()
            try:
                lat = str(round(coords[0] - float(data[2]), 8))
                longit = str(round(coords[1] - float(data[3]), 8))
                print(lat + "," + longit) #Testing
                if not self.stop_thread.is_set():
                    if self.map == True:
                        # Map widget goes here
                        test = 0
                    else:
                        self.frame.received_location_value.configure(text= str(round(coords[0], 8)) + ", " + str(round(coords[1], 8)))
                        self.frame.calculated_differential_value.configure(text= data[2] + ", " + data[3])
                        self.frame.actual_location_value.configure(text= lat + ", " + longit)
            except:
                print("conversion error")
                continue
    
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
        if self.map == True:
            self.frame.map_button.configure(text="Map View")
            self.frame.map_group.lower()
        else:
            self.frame.map_button.configure(text="Stats View")
            self.frame.map_group.lift()
            
    def use_current_coords(self):
        while True:
            coords = getCoords()
            try:
                self.frame.base_latitude_button.configure(text= str(round(coords[0]), 8))
                self.frame.base_longitude_button.configure(text= str(round(coords[1]), 8))
                break
            except:
                continue
        
    def showNumericEntry(self, input_type):
        self.numeric_entry_controller = NumericEntryController(self.frame, self.model, input_type, self)
        self.numeric_entry_controller.view.grid(row=0, column=0, rowspan=4, columnspan=6, padx=0, pady=0, sticky="nsew")
        
    def stop(self):
        self.stop_thread.set()
        # self.GPS.join()
        self.GPS = None