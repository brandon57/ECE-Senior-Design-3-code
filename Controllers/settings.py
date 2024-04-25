from Views.numericentry import NumericEntry
from Controllers.numericentry import NumericEntryController


class Settings_Controller:
    
    # I just had this here for testing, probs should be in model?
    on = 0
    mode = 0 
    map = 0

    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.frame = self.view.frames["settings"]

        self.configure()
        
    def configure(self):

        self.frame.stop_button.configure(command=lambda: self.changeState(not Settings_Controller.on))        
        self.frame.change_mode_button.configure(command=lambda: self.changeMode(not Settings_Controller.mode))        
        self.frame.map_button.configure(command=lambda: self.showMap(not Settings_Controller.map))        
        self.frame.base_latitude_button.configure(command=lambda: self.showInput(not Settings_Controller.input))  

        self.frame.base_latitude_button.configure(command=lambda: self.showNumericEntry('latitude'))
        self.frame.base_longitude_button.configure(command=lambda: self.showNumericEntry('longitude'))

        self.changeState(0) # OFF at program start
        self.changeMode(0) # Initalize in receiver mode
        self.showMap(0) # Hide map on startup
    
    def changeState(self, on):
        Settings_Controller.on = on
        if on == 0:
            self.frame.stop_button.configure(text="Start", fg_color="green")
            self.showMap(0)
            self.frame.change_mode_button.lift()
            

        else:
            self.frame.stop_button.configure(text="STOP", fg_color="darkred")
            self.frame.change_mode_button.lower()

    def changeMode(self, mode):
        Settings_Controller.mode = mode
        if mode == 0:
            self.frame.mode_label.configure(text="This device is in mobile receiver mode")
            self.frame.base_location_group.lower()
            self.frame.receiver_group.lift()
        else:
            self.frame.mode_label.configure(text="This device is in base station mode")
            self.frame.receiver_group.lower()
            self.frame.base_location_group.lift()
    
    def showMap(self, map):
        Settings_Controller.map = map
        if self.map == 0:
            self.frame.map_button.configure(text="Map View")
            self.frame.map_group.lower()
        else:
            self.frame.map_button.configure(text="Stats View")
            self.frame.map_group.lift()

    def showNumericEntry(self, input_type):
        self.numeric_entry_controller = NumericEntryController(self.frame, self.model, input_type, self)
        self.numeric_entry_controller.view.grid(row=0, column=0, rowspan=4, columnspan=6, padx=0, pady=0, sticky="nsew")