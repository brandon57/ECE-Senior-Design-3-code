from threading import *
from IO.COMS import *
from IO.GPS_I2C import getCoords

class MainFrame_Controller():
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.frame = self.view.frames["mainframe"]
        self.on = False
        
        self.configure()
        
        self.GPS = None
        self.stop_thread = Event()
    
    def configure(self): # Configures the buttons
        self.frame.start_button.configure(command=self.start)
        self.frame.modeButton.config(command=self.changeMode)
        self.frame.settings_button.config(command= lambda: self.view.change_frame("settings"))
        self.frame.map_button.config(command= lambda: self.view.change_frame("map"))
    
    def start(self):
        if self.stop_thread:
            self.stop_thread.clear()
        self.on = not self.on
        
        if self.on == False:
            self.frame.startButton_text.set("Start")
            self.stop()
        else:
            self.frame.startButton_text.set("Stop")
            # self.frame.update_start("Stop")
            #startButton_text.set("Stop")
            if self.model.get_mode() != 0:
                self.GPS = Thread(target= lambda: self.Sender, daemon=True)
            else:
                self.GPS = Thread(target= lambda: self.Receiver, daemon=True)
            self.GPS.start()
    
    def Sender(self):
        while not self.stop_thread.is_set():
            coords = getCoords() # grabs coordinates
            user_coords = self.model.get_coords()
            try:
                lat_diff = str(-(user_coords[0] - coords[0]))
                longit_diff = str(-(user_coords[1] - coords[1]))
                print(coords) #Testing
                # sendData(lat + "," + longit)
                if not self.stop_thread.is_set():
                    sendData(lat_diff + "," + longit_diff)
                    # self.frame.update_coords(str(coords[0]), str(coords[1]))
                    # latNum_text.set(str(coords[0]))
                    # longNum_text.set(str(coords[1]))
            except:
                continue
    
    def Receiver(self):
        while not self.stop_thread.is_set():
            data = receiveData().split(",")
            print(data) #Testing
            
            coords = getCoords()
            try:
                lat = str(round(coords[0] - float(data[2]), 4))
                longit = str(round(coords[1] - float(data[3]), 4))
                print(lat + "," + longit) #Testing
                self.frame.latNum_text.set(lat)
                self.frame.longNum_text.set(longit)
                # self.frame.update_coords(lat, longit)
                # latNum_text.set(lat)
                # longNum_text.set(longit)
            except:
                print("conversion error")
                continue
    
    def changeMode(self):
        self.model.change_mode()
        if self.model.get_mode() == 0:
            self.frame.modeButton_text.set("Receiver")
        else:
            self.frame.modeButton_text.set("Sender")
        
    def stop(self):
        self.stop_thread.set()
        # self.GPS.join()
        
        self.GPS = None